from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.db.database import init_db, seed_demo_data

app = FastAPI(
    title="SanjivaniGPT API",
    description="AI ecosystem for Sanjivani University",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(chat_router)


@app.on_event("startup")
def startup():
    init_db()
    seed_demo_data()


@app.get("/")
def root():
    return {
        "message": "Welcome to SanjivaniGPT",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SanjivaniGPT Backend",
    }
