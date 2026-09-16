from src.database.database import SessionLocal
from src.repository.note_repository import NoteRepository
from src.services.note_service import NoteService

session = SessionLocal()

repository = NoteRepository(session)

service = NoteService(repository)