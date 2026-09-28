from data_base.data_base import Database
from utils.note_logger import logger
from utils.note_types import NoteFactory
from storage.json_storage import JsonStorage


class NoteRepository:

    def __init__(self, storage: JsonStorage) -> None:
        self.storage = storage

    def load(self) -> Database:
        try:
            data = self.storage.load()

            notes = [
                NoteFactory.from_dict(item)
                for item in data["notes"]
            ]

            return Database(
                notes=notes,
                last_id=data["last_id"]
            )



        except KeyError as ke:
            logger.error("Missing key in JSON data: %s", ke)
            raise

        except ValueError as ve:
            logger.error("Invalid note data: %s", ve)
            raise

    def save(self, db: Database) -> None:
        try:
            data = {
                "last_id": db.last_id,
                "notes": [note.to_dict() for note in db.notes]
            }

            self.storage.save(data)

        except OSError as oe:
            logger.error("Failed to save notes: %s", oe)
            raise

    def delete(self, db: Database, note_id: int) -> None:
        try:
            for i, note in enumerate(db.notes):
                if note.id == note_id:
                    db.notes.pop(i)
                    self.save(db)
                    return

            logger.warning("Note %s was not found.", note_id)

        except OSError as oe:
            logger.error("Failed to delete note %s: %s", note_id, oe)
            raise
