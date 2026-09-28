from storage.json_storage import JsonStorage
from pathlib import Path
from repository.note_repository import NoteRepository
from services.note_service import NoteService

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "notes.json"

storage = JsonStorage(DATA_FILE)
repository = NoteRepository(storage)
service = NoteService(repository)