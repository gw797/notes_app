
from utils.note_logger import logger
from models.base_note import BaseNote
from utils.note_types import NoteFactory


class NoteService:

    def __init__(self, repository):
        self.repository = repository
        self.db = repository.load()

    def get_all_notes(self):
        return self.db.notes

    def get_note_by_id(self, note_id):
        for note in self.db.notes:
            if note.id == note_id:
                logger.info("Note %s found.", note_id)
                return BaseNote.__str__(note)

        logger.warning("Note %s does not exist.", note_id)
        return None

    def _add_note(self, note):
        self.db.notes.append(note)
        self.repository.write(self.db)

        logger.info("Note %s created successfully.", note.id)

        return note

    def create(self, note_type, title, content):
        try:
            note_id = self.db.get_next_id()

            note = NoteFactory.create(
                note_type,
                title,
                content,
                note_id
            )

            return self._add_note(note)

        except ValueError as ve:
            logger.error("Note type does not exist: %s", ve)
            return None

    def update_note(self, note_id, **kwargs):
        note = self.get_note_by_id(note_id)

        if note is None:
            return None

        for field, value in kwargs.items():
            if value is not None:
                setattr(note, field, value)

        self.repository.write(self.db)

        logger.info("Note %s updated successfully.", note_id)

        return note

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)

        if note is None:
            return None

        self.db.notes.remove(note)
        self.repository.write(self.db)

        logger.info("Note %s deleted successfully.", note_id)

        return note

