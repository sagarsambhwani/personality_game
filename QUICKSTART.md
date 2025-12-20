# Personality Game - Quick Start Guide

## Running the Application

### Terminal 1 - Backend
```bash
cd c:\Users\user\Downloads\personality_test\personality_game\backend\ai_langgraph_project
python -m uvicorn app.main:app --reload
```
✅ Backend will run on http://localhost:8000

### Terminal 2 - Frontend
```bash
cd c:\Users\user\Downloads\personality_test\personality_game\frontend\Client
npm run dev
```
✅ Frontend will run on http://localhost:5173

## Usage
1. Open http://localhost:5173 in your browser
2. Fill in the profile form
3. Click "Start Analysis"
4. Wait 2-3 minutes for AI processing
5. View your MBTI personality results!

## Notes
- Ensure you have `GOOGLE_API_KEY` in backend `.env` file
- The process takes 2-3 minutes due to AI image generation
- PostgreSQL database is optional (fallback implemented)

## Project Structure
```
personality_game/
├── backend/ai_langgraph_project/    # FastAPI + LangGraph
└── frontend/Client/                  # React + Vite + Tailwind
```
