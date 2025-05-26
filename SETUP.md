# 🎓 AI Tutor Multi-Agent System

## Project Overview

The AI Tutor Multi-Agent System is a FastAPI-based educational platform that uses a network of specialized AI agents to provide personalized tutoring across various subjects. The system features a beautiful, animated chatbot UI and intelligently routes questions to the appropriate specialist agent.

**Architecture:**

- **Backend**: FastAPI server with Google ADK integration
- **Frontend**: Single-file HTML with Alpine.js and Tailwind CSS
- **Agent System**: Root orchestrator with specialist agents for different subjects

## Setup Instructions

### Prerequisites

- Python 3.9+ installed
- Google ADK access (optional, system works in fallback mode without it)

### Installation Steps

1. **Clone the repository or extract the project files**

2. **Install dependencies:**

```bash
pip install fastapi uvicorn python-dotenv pydantic google-adk langchain-community tavily-python sympy matplotlib numpy 
```

4. **Configure Environment Variables:**

Create a `.env` file in the root directory with:

```
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here  # Optional for web search
```

## Running the Application

1. **Start the server:**

```bash
python start.py
```

2. **Access the application:**

Open your browser and navigate to: http://localhost:8000

## Live Demo

[Access the live demo here](#) <!-- You'll add the actual link when deployed -->

## How It Works

### Agent System

The system consists of a root orchestrator agent that analyzes user queries and delegates to specialist agents:

- **Math Agent**: Handles algebra, calculus, equation solving
- **Physics Agent**: Provides constants, unit conversions, physics calculations
- **Biology Agent**: Specializes in cell biology, genetics, organism classification
- **Chemistry Agent**: Processes elements, reactions, molecular calculations
- **Web Search Agent**: Retrieves current information and real-time data

### Tool Integration

Each agent has access to domain-specific tools:

- Math tools for calculation and equation solving
- Physics tools for constants lookup and unit conversions
- Biology tools for genetics and organism classification
- Chemistry tools for element information and reaction calculations

### Session Management

The system maintains user sessions with:

- Unique user IDs and session IDs
- Conversation history tracking
- "New Session" functionality to start fresh conversations


