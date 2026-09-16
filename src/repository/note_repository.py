import json
from utils.note_logger import logger

from data_base.data_base import Database
from utils.note_types import NoteFactory


class NoteRepository:

    def __init__(self, filename: str) -> Database:
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

        except FileNotFoundError:
            return Database()

        notes = [
            NoteFactory.from_dict(item)
            for item in data["notes"]
        ]

        return Database(
            notes=notes,
            last_id=data["last_id"]
        )

    def save(self, note):
        try:
            db = self.load()

            db.notes.append(note)

            self.write(db)

        except FileNotFoundError:
            logger.warning("File not found")

    def update(self, note):
        try:
            db = self.load()

            for i, existing_note in enumerate(db.notes):
                if existing_note.id == note.id:
                    db.notes[i] = note
                    self.write(db)
                    return

            logger.warning("Note %s not found", note.id)

        except FileNotFoundError:
            logger.warning("File not found")

    def delete(self, note_id):
        try:
            db = self.load()

            for i, note in enumerate(db.notes):
                if note.id == note_id:
                    db.notes.pop(i)
                    self.write(db)
                    return

            logger.warning("Note %s not found", note_id)

        except FileNotFoundError:
            logger.warning("File not found")

    def write(self, db):
        data = {
            "last_id": db.last_id,
            "notes": [note.to_dict() for note in db.notes]
        }

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
