# Personality Game - AI-Powered Personality Assessment PoC

> **An intelligent personality analysis system** that generates personalized visual scenarios and determines your MBTI type through AI-driven psychological assessment.

![Status](https://img.shields.io/badge/status-PoC%20Complete-success)
![Backend](https://img.shields.io/badge/backend-FastAPI%20%2B%20LangGraph-blue)
![Frontend](https://img.shields.io/badge/frontend-React%20%2B%20Vite-purple)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)

---

## 🎯 What is This?

This is a **Proof of Concept (PoC)** for an AI-powered personality assessment system that:

1. **Takes your profile** (name, age, profession, etc.)
2. **Generates personalized visual scenarios** using Google Gemini's image generation
3. **Creates psychological questions** based on those visuals
4. **Determines your MBTI personality type** through AI analysis

The entire process takes 2-3 minutes and runs completely automated through a sophisticated LangGraph workflow.

---

## 🏗️ Architecture

### System Overview

```
┌─────────────┐         ┌──────────────┐         ┌─────────────────┐
│   React     │ ──────> │   FastAPI    │ ──────> │   LangGraph     │
│  Frontend   │ <────── │   Backend    │ <────── │   Workflow      │
└─────────────┘         └──────────────┘         └─────────────────┘
                                                           │
                                                           │
                                                           ▼
                                                  ┌─────────────────┐
                                                  │  Google Gemini  │
                                                  │      APIs       │
                                                  └─────────────────┘
```

### LangGraph Workflow (6 Sequential Nodes)

```
user_profile → prompt_generation → image_generation → 
mcq_generation → mbti_analysis → final_response
```

Each node is an AI-powered step that transforms the data:

| Node | What It Does | Duration |
|------|-------------|----------|
| `user_profile` | Analyzes demographics → creates personality sketch | ~15s |
| `prompt_generation` | Generates 3-5 visual scenario prompts | ~15s |
| `image_generation` | Creates PNG images from prompts | ~90s |
| `mcq_generation` | Analyzes images → creates MCQ questions | ~45s |
| `mbti_analysis` | Determines MBTI type from answers | ~15s |
| `final_response` | Formats final output | <1s |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+** (backend)
- **Node.js 18+** (frontend)
- **Google API Key** with Gemini access ([Get it here](https://ai.google.dev/))

### Setup & Run

**Step 1: Clone & Configure**
```bash
cd personality_game/backend/ai_langgraph_project
```

Create `.env` file:
```env
GOOGLE_API_KEY=your_google_api_key_here
# Optional: PGVECTOR_CONN=postgresql://... (fallback implemented)
```

**Step 2: Install Dependencies**
```bash
# Backend
cd backend/ai_langgraph_project
pip install -r requirements.txt

# Frontend
cd ../../frontend/Client
npm install
```

**Step 3: Run Both Servers**

Terminal 1 (Backend):
```bash
cd backend/ai_langgraph_project
python -m uvicorn app.main:app --reload
```
✅ Backend: http://localhost:8000

Terminal 2 (Frontend):
```bash
cd frontend/Client
npm run dev
```
✅ Frontend: http://localhost:5173

**Step 4: Test It Out!**
1. Open http://localhost:5173
2. Fill in your profile
3. Click "Start Analysis"
4. Wait 2-3 minutes
5. See your MBTI results!

---

## 📂 Project Structure

```
personality_game/
├── backend/ai_langgraph_project/
│   ├── app/
│   │   ├── api/v1/endpoint/
│   │   │   ├── chatbot.py           # Main /analyze endpoint
│   │   │   └── workflow_nodes.py     # Individual node endpoints
│   │   ├── core/
│   │   │   └── llm_factory.py        # LLM provider + rate limiting
│   │   ├── langgraph_app/
│   │   │   ├── agents/               # 6 workflow nodes
│   │   │   │   ├── user_profile.py
│   │   │   │   ├── prompt_generation.py
│   │   │   │   ├── image_generation.py
│   │   │   │   ├── mcq_generation.py
│   │   │   │   ├── mbti_analysis.py
│   │   │   │   └── response.py
│   │   │   └── workflows/
│   │   │       └── chatbot_graph.py  # Graph definition
│   │   ├── schemas/
│   │   │   └── chat.py               # Pydantic data models
│   │   └── main.py                   # FastAPI app
│   ├── outputs/                      # Generated images
│   ├── test_pipeline.py              # Standalone test
│   └── requirements.txt
│
└── frontend/Client/
    ├── src/
    │   ├── components/
    │   │   ├── ProfileForm.jsx       # User input form
    │   │   ├── LoadingView.jsx       # Animated loading
    │   │   └── ResultsView.jsx       # Results display
    │   ├── App.jsx                   # Main app logic
    │   ├── main.jsx                  # React entry
    │   └── index.css                 # Tailwind styles
    ├── package.json
    └── vite.config.js                # Vite + API proxy
```

---

## 🎨 UI Features

### Modern Glassmorphism Design
- 🌈 Purple gradient background
- 🪞 Frosted glass effects
- ✨ Smooth animations
- 📱 Responsive layout

### User Flow
1. **Input Screen**: Form with validation (name, age, gender, profession, nationality)
2. **Loading Screen**: Animated progress indicators with step descriptions
3. **Results Screen**: MBTI type, profile analysis, statistics, and reset option

---

## 🔧 Technical Highlights

### Backend
- **FastAPI**: Async REST API with automatic OpenAPI docs
- **LangGraph**: Stateful workflow orchestration
- **Pydantic v2**: Type-safe data validation
- **Rate Limiting**: Automatic 15s delays for Gemini Free Tier (5 RPM)
- **Fallback Logic**: Works without PostgreSQL (pure LLM analysis)

### Frontend
- **React 18**: Modern hooks-based architecture
- **Vite**: Lightning-fast dev server with HMR
- **Tailwind CSS**: Utility-first styling
- **Lucide Icons**: Beautiful SVG icons
- **API Proxy**: Seamless backend integration

### AI Models
- **gemini-1.5-flash**: Text analysis (profile, prompts, MBTI)
- **gemini-2.5-flash-image-preview**: Image generation
- **gemini-1.5-flash** (vision): Image → MCQ generation

---

## 🧪 Testing

### Backend Only
```bash
cd backend/ai_langgraph_project
python test_pipeline.py
```

### API Test
```bash
curl -X POST http://localhost:8000/api/v1/personality/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice",
    "age": 28,
    "gender": "Female",
    "profession": "Designer",
    "nationality": "Canadian"
  }'
```

### Full E2E
Run both servers and test via browser at http://localhost:5173

---

## 📊 API Endpoints

### Main Endpoint
- **POST** `/api/v1/personality/analyze`
  - Input: Profile object (name, age, gender, profession, nationality)
  - Output: Complete analysis with MBTI result, images count, MCQs count

### Debug Endpoints (Individual Nodes)
- **POST** `/api/v1/nodes/user-profile`
- **POST** `/api/v1/nodes/prompt-generation`
- **POST** `/api/v1/nodes/image-generation`
- **POST** `/api/v1/nodes/mcq-generation`
- **POST** `/api/v1/nodes/mbti-analysis`

### Health Checks
- **GET** `/health`
- **GET** `/api/v1/personality/health`

Swagger docs: http://localhost:8000/docs

---

## 🔒 Environment Variables

**Required:**
```env
GOOGLE_API_KEY=your_api_key_here
```

**Optional:**
```env
PGVECTOR_CONN=postgresql+psycopg://user:pass@localhost:5432/mbti
GROQ_API_KEY=your_groq_key  # For faster LLM alternative
```

---

## ⚠️ Known Limitations (PoC)

1. **No Real MCQ Interaction**: Questions are generated but users don't answer them
2. **Mock Analysis**: MBTI determination uses the questions themselves, not user answers
3. **No Image Display**: Generated images stay on backend (in `outputs/`)
4. **No Progress Streaming**: Loading screen is static
5. **Single Session**: No state persistence or multi-user support
6. **Rate Limits**: Free Gemini tier = 5 requests/minute (enforced via sleep)

---

## 🚀 Future Enhancements

- [ ] Real MCQ interaction flow
- [ ] Image display in frontend
- [ ] WebSocket for real-time progress
- [ ] User answer collection & analysis
- [ ] Session management
- [ ] Database for results storage
- [ ] Deployment configuration (Docker, cloud)

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🙏 Credits

**Technologies Used:**
- [Google Gemini](https://ai.google.dev/) - AI models
- [LangGraph](https://github.com/langchain-ai/langgraph) - Workflow orchestration  
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [React](https://react.dev/) - Frontend framework
- [Vite](https://vitejs.dev/) - Build tool
- [Tailwind CSS](https://tailwindcss.com/) - Styling

---

## 📧 Questions?

This is a PoC demonstrating AI-powered personality assessment through visual scenarios and LangGraph workflows. For production use, consider implementing the enhancements listed above.

**Enjoy exploring your personality! 🎭**
