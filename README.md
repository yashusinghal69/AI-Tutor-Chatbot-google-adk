# AI Tutor Multi-Agent System

A sophisticated educational chatbot powered by Google's Agent Development Kit (ADK) that provides personalized tutoring across multiple subjects including Mathematics, Physics, Biology, Chemistry and Web search for geneal query.

## 🎯 Project Overview

This AI Tutor system employs a multi-agent architecture where specialized agents collaborate to provide comprehensive educational support. The system features:

- **Orchestrator Agent**: Coordinates between specialized agents and manages conversation flow
- **Subject Specialists**: Dedicated agents for Math, Physics, Biology, and Chemistry
- **Web Search Agent**: Provides real-time information and current data
- **Session Management**: Maintains conversation context and learning progress
- **Interactive Web Interface**: User-friendly chat interface for seamless interaction

## 🏗️ Architecture

### Multi-Agent System

```
┌─────────────────┐     ┌─────────────────┐
│   User Query    │────▶│   Root Agent    │
└─────────────────┘     │  (Orchestrator) │
                        └─────────┬───────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼
┌─────────────┐          ┌─────────────┐          ┌─────────────┐
│ Math Agent  │          │Physics Agent│          │Biology Agent│
│             │          │             │          │             │
│ Tools:      │          │ Tools:      │          │ Tools:      │
│• Calculator │          │• Constants  │          │• Organism   │
│• Equations  │          │• Units      │          │• Genetics   │
│• Graphing   │          │• Physics    │          │• DNA        │
└─────────────┘          └─────────────┘          └─────────────┘
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼
┌─────────────┐          ┌─────────────┐          ┌─────────────┐
│Chemistry    │          │Web Search   │          │   Session   │
│Agent        │          │Agent        │          │ Management  │
│             │          │             │          │             │
│ Tools:      │          │ Tools:      │          │• History    │
│• Elements   │          │• Tavily     │          │• Context    │
│• Reactions  │          │• Real-time  │          │• Progress   │
│• Molarity   │          │• Current    │          │             │
└─────────────┘          └─────────────┘          └─────────────┘
```

### Agent Capabilities

#### Math Agent

- **Expression Calculation**: Evaluates mathematical expressions
- **Equation Solving**: Solves algebraic and calculus equations
- **Graph Generation**: Creates visual representations of functions

#### Physics Agent

- **Physical Constants**: Access to fundamental physics constants
- **Unit Conversion**: Converts between different measurement units
- **Physics Calculations**: Performs complex physics computations

#### Biology Agent

- **Organism Classification**: Taxonomic information and classification
- **Genetics Calculations**: Genetic probability and inheritance patterns
- **DNA Operations**: DNA sequence analysis and complement generation

#### Chemistry Agent

- **Element Information**: Periodic table data and element properties
- **Molecular Mass**: Calculates molar masses of compounds
- **Chemical Equations**: Balances chemical reactions
- **Solution Chemistry**: pH and molarity calculations

#### Web Search Agent

- **Real-time Information**: Current events and updated information
- **Academic Resources**: Access to educational content online
- **Fact Verification**: Cross-references information from multiple sources

## 🚀 Getting Started

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yashusinghal69/AI-Tutor-Chatbot-google-adk.git

   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:

   ```env
   TAVILY_API_KEY=your-tavily-api-key
   GOOGLE_API_KEY=your-google-api-key
   GEMINI_API_KEY=your-google-api-key
    
   ```

### Running the Application

1. **Start the FastAPI server**

   ```bash
   python main.py
   ```

   Or using uvicorn directly:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`
   - The API documentation is available at `http://localhost:8000/docs`

## 🌐 Live Deployment

The application is deployed and accessible at: [Your Deployment URL]


## 🛠️ Development

### Project Structure

```
ai-tutor-chatbot/
├── app/
│   ├── __init__.py
│   ├── agent.py              # Root agent implementation
│   └── agents/               # Specialized agents
│       ├── math_agent.py
│       ├── physics_agent.py
│       ├── biology_agent.py
│       ├── chemistry_agent.py
│       └── web_search_agent.py
├── templates/
│   └── index.html            # Web interface
├── static/                   # CSS, JS, images
├── main.py                   # FastAPI application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
└── README.md                 # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support, email [chaman_s@mt.iitr.ac.in] or create an issue in the GitHub repository.


