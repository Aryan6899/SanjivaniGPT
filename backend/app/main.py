from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

# import chat API
from app.api.chat import router as chat_router

app = FastAPI(
    title="SanjivaniGPT API",
    description="AI ecosystem for Sanjivani University",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to SanjivaniGPT",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SanjivaniGPT Backend"
    }