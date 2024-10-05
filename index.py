from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.note import note

app = FastAPI()

# Mounting static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Including the note router
app.include_router(note, prefix="/notes")  # You can set a prefix for better routing
