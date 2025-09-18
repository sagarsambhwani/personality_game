# User Profile Analysis System

This project implements a user profile analysis system using FastAPI, LangGraph, and Google Gemini LLM. The system allows you to create, read, update, and delete user profiles, as well as analyze user profiles using the Google Gemini LLM.

## Features

- CRUD operations for user profiles
- User profile analysis using Google Gemini LLM
- LangGraph workflow for user analysis
- FastAPI endpoints for all operations

## Project Structure

```
├── app/
│   ├── crud/            # CRUD operations
│   ├── database.py      # Database configuration
│   ├── langgraph/       # LangGraph workflows
│   │   ├── graph.py     # LangGraph workflow definitions
│   │   └── nodes/       # LangGraph nodes
│   ├── main.py          # FastAPI application
│   ├── models/          # SQLAlchemy models
│   ├── routes/          # FastAPI routes
│   ├── schemas/         # Pydantic schemas
│   └── services/        # Services (LLM, etc.)
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Google API key: `GOOGLE_API_KEY=your_api_key`
4. Run the application: `uvicorn app.main:app --reload`

## API Endpoints

### User Profiles

- `POST /api/v1/user-profiles/`: Create a new user profile
- `GET /api/v1/user-profiles/{user_profile_id}`: Get a user profile by ID
- `GET /api/v1/user-profiles/`: Get all user profiles
- `PUT /api/v1/user-profiles/{user_profile_id}`: Update a user profile
- `DELETE /api/v1/user-profiles/{user_profile_id}`: Delete a user profile

### User Analysis

- `POST /api/v1/analyze-user/`: Analyze a user profile using Google Gemini LLM

## Example Usage

### Analyze a User Profile

```python
import requests

url = "http://localhost:8000/api/v1/analyze-user/"
data = {
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "nationality": "American",
    "profession": "Software Engineer"
}

response = requests.post(url, json=data)
print(response.json())
```

## License

MIT
