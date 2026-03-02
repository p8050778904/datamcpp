# AI-Driven Analytics Dashboard

Flexible analytics dashboard with Natural Language to MongoDB Aggregation Pipeline translation.

## Tech Stack
- **Frontend**: React, Axios, Recharts, Lucide-React
- **Backend**: FastAPI, Motor (MongoDB), Pydantic
- **Database**: MongoDB (Regions, Employees, Products, Sales)

## Getting Started

### Prerequisites
- MongoDB running locally on `localhost:27017`
- Python 3.9+
- Node.js 16+

### Backend Setup
1. `cd backend`
2. `pip install -r requirements.txt`
3. Seed data: `$env:PYTHONPATH=".."; python app/database/seed.py`
4. Run server: `uvicorn app.main:app --reload`

### Frontend Setup
1. `cd frontend`
2. `npm install`
3. `npm run dev`

## Deployment Architecture
`User → React (Vite) → FastAPI (Uvicorn) → MongoDB`
The AI layer (MCP/LLM) is integrated into the FastAPI service layer to interpret user queries dynamically.
