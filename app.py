from fastapi import FastAPI
from dotenv import load_dotenv
from tasks import text, image, audio

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Frugal AI Challenge API",
    description="API for the Frugal AI Challenge evaluation endpoints"
)

# Include all routers
app.include_router(text.router)
app.include_router(image.router)
app.include_router(audio.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Frugal AI Challenge API",
        "endpoints": {
            "text": "/text - Text classification task",
            "image": "/image - Image classification task (coming soon)",
            "audio": "/audio - Audio classification task (coming soon)"
        }
    } 