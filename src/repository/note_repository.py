import json
from utils.note_logger import logger

from data_base.data_base import Database
from utils.note_types import NoteFactory
from storage.json_storage import JsonStorage


class NoteRepository:

    def __init__(self, storage: JsonStorage):
        self.storage = storage

    def load(self)->Database:
        data = self.storage.load()

        notes = [
            NoteFactory.from_dict(item)
            for item in data["notes"]
        ]

        return Database(
            notes=notes,
            last_id=data["last_id"]
        )


    def save(self, db: Database)-> None:
      data = {
          "last_id": db.last_id,
          "notes": [note.to_dict() for note in db.notes]
      }

      self.storage.save(data)



    def delete(self, db:Database, note_id:int)-> None:
        try:

            for i, note in enumerate(db.notes):
                if note.id == note_id:
                    db.notes.pop(i)
                    self.save(db)
                    return



        except FileNotFoundError:
            logger.warning("File not found")

