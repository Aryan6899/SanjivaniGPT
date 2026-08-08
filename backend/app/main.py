from fastapi import FastAPI

app = FastAPI(
    title="SanjivaniGPT API",
    description="AI ecosystem for Sanjivani University",
    version="0.1.0"
)


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