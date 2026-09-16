from repository.note_repository import NoteRepository
from services.note_service import NoteService

repository = NoteRepository("data/notes.json")
service = NoteService(repository)