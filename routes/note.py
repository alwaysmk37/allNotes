from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn  # Make sure this is configured correctly
from schemas.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    docs = conn.notes.notes.find()  # Fetching notes from the database
    newDocs = list(docs)  # Convert to a list if necessary
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def create_note(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    conn.notes.notes.insert_one(formDict)
    return {"Success": True}
