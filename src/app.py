from storage.json_storage import JsonStorage
from repository.note_repository import NoteRepository
from services.note_service import NoteService
storage = JsonStorage("data/notes.json")
repository = NoteRepository(storage)
service = NoteService(repository)