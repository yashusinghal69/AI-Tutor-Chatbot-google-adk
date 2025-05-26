from typing import Optional
import asyncio
import os
import uuid
from pathlib import Path
from datetime import datetime
import json
import logging
import sys

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel



from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
# Import your root agent
from app.agent import root_agent
ADK_AVAILABLE = True


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Tutor Multi-Agent System", version="1.0.0")

# Templates configuration
templates = Jinja2Templates(directory="templates")

# Session service and runner for Google ADK

session_service = InMemorySessionService()
    # Initialize Runner with required parameters
runner = Runner(
        agent=root_agent,
        app_name="ai_tutor_app",
       session_service=session_service
)
    
# Global constants for ADK
APP_NAME = "ai_tutor_app"


# In-memory storage for sessions (you can replace with Redis/Database)
sessions_storage = {}

class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = None
    user_id: Optional[str] = None

class QueryResponse(BaseModel):
    response: str
    session_id: str
    user_id: str
    agent_used: str

class SessionRequest(BaseModel):
    user_id: str

class SessionResponse(BaseModel):
    session_id: str
    user_id: str
    created_at: str
    message: str

def create_new_session(user_id: str) -> str:
    """Create a new session for a user"""
    session_id = f"session_{uuid.uuid4().hex[:8]}"
    sessions_storage[session_id] = {
        "user_id": user_id,
        "created_at": datetime.now().isoformat(),
        "conversation_history": [],
        "context": {}
    }
    return session_id

def get_session_data(session_id: str):
    """Get session data"""
    return sessions_storage.get(session_id)

def add_to_conversation_history(session_id: str, role: str, message: str):
    """Add message to conversation history"""
    if session_id in sessions_storage:
        sessions_storage[session_id]["conversation_history"].append({
            "role": role,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })

async def call_agent_async(query: str, user_id: str, session_id: str) -> str:
    """Call the agent using proper Google ADK API"""
    if not ADK_AVAILABLE or not runner or not types:
        return None
    
    try:
        # Create session if it doesn't exist in ADK
        try:
            session = await session_service.create_session(
                app_name=APP_NAME,
                user_id=user_id,
                session_id=session_id
            )
        except Exception:
            # Session might already exist
            pass
        
        # Prepare the user's message in ADK format
        content = types.Content(role='user', parts=[types.Part(text=query)])
        
        final_response_text = "Agent did not produce a final response."
        
        # Use run_async with proper parameters
        async for event in runner.run_async(
            user_id=user_id, 
            session_id=session_id, 
            new_message=content
        ):
            # Check for final response
            if event.is_final_response():
                if event.content and event.content.parts:
                    final_response_text = event.content.parts[0].text
                elif event.actions and event.actions.escalate:
                    final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
                break
        
        return final_response_text
        
    except Exception as e:
        logger.error(f"ADK call_agent_async error: {e}")
        return f"Error processing request: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        user_id = request.user_id or "anonymous_user"
        session_id = request.session_id
        
        # Create session if not provided
        if not session_id:
            session_id = create_new_session(user_id)
        
        # Validate session exists
        session_data = get_session_data(session_id)
        if not session_data:
            session_id = create_new_session(user_id)
            session_data = get_session_data(session_id)
          # Validate user_id matches session
        if session_data["user_id"] != user_id:
            raise HTTPException(status_code=400, detail="User ID mismatch with session")
        
        logger.info(f"Processing query for user {user_id}, session {session_id}: {request.query}")
        
        # Process query with the root agent using Google ADK Runner
        if ADK_AVAILABLE and runner and root_agent:
            try:
                response_text = await call_agent_async(request.query, user_id, session_id)
                if not response_text:
                    response_text = "I apologize, but I couldn't process your request."
            except Exception as e:
                logger.error(f"ADK Runner error: {e}")
                response_text = "I apologize, but I'm currently unable to process your request. Please try again later."
        else:
            # Fallback mode - simple response
            response_text = f"🎓 **AI Tutor Response (Fallback Mode)**\n\nI received your query: '{request.query}'\n\n⚠️ **Note**: The full multi-agent system requires Google ADK to be properly configured. Currently running in demo mode.\n\n💡 **What I can help with**:\n- Mathematics (algebra, calculus, equations)\n- Physics (mechanics, constants, conversions)\n- Biology (cells, genetics, organisms)\n- Chemistry (elements, reactions, calculations)\n- General educational questions\n\nPlease set up the Google ADK environment for full functionality."
        
        # Update conversation history
        add_to_conversation_history(session_id, "user", request.query)
        add_to_conversation_history(session_id, "assistant", response_text)
        
        logger.info(f"Response generated for session {session_id}")
        
        return QueryResponse(
            response=response_text,
            session_id=session_id,
            user_id=user_id,
            agent_used="ai_tutor_orchestrator"
        )
        
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/session/new", response_model=SessionResponse)
async def create_session_endpoint(request: SessionRequest):
    try:
        session_id = create_new_session(request.user_id)
        session_data = get_session_data(session_id)
        
        logger.info(f"New session created: {session_id} for user: {request.user_id}")
        
        return SessionResponse(
            session_id=session_id,
            user_id=request.user_id,
            created_at=session_data["created_at"],
            message="New session created successfully"
        )
        
    except Exception as e:
        logger.error(f"Error creating session: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/session/{session_id}")
async def get_session(session_id: str):
    session_data = get_session_data(session_id)
    if not session_data:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return session_data


@app.delete("/api/session/{session_id}")
async def clear_session(session_id: str):
    """Clear a specific session"""
    if session_id in sessions_storage:
        del sessions_storage[session_id]
        return {"message": "Session cleared successfully"}
    else:
        raise HTTPException(status_code=404, detail="Session not found")


@app.get("/api/agents")
async def get_agents():
    return {
        "tutor": {
            "id": "ai_tutor_orchestrator",
            "name": "AI Tutor Orchestrator", 
            "type": "orchestrator"
        },
        "specialists": {
            "math": {
                "id": "math_agent",
                "name": "Math Tutor Agent",
                "capabilities": ["calculations", "equation solving", "graphing"],
                "tools": ["calculate_expression", "solve_equation", "create_graph"]
            },
            "physics": {
                "id": "physics_agent", 
                "name": "Physics Tutor Agent",
                "capabilities": ["constants lookup", "unit conversions", "physics calculations"],
                "tools": ["get_physics_constant", "convert_units", "calculate_physics"]
            },
            "biology": {
                "id": "biology_agent",
                "name": "Biology Tutor Agent", 
                "capabilities": ["biological information", "organism classification", "genetics"],
                "tools": ["get_biology_info", "classify_organism", "calculate_genetics", "get_dna_complement"]
            },
            "chemistry": {
                "id": "chemistry_agent",
                "name": "Chemistry Tutor Agent",
                "capabilities": ["element information", "molecular calculations", "chemical reactions"],
                "tools": ["get_element_info", "calculate_molar_mass", "balance_equation", "calculate_molarity", "calculate_ph"]
            },
            "web_search": {
                "id": "web_search_agent",
                "name": "Web Search Agent",
                "capabilities": ["current information", "real-time data", "web search"],
                "tools": ["tavily_search"]
            }
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
