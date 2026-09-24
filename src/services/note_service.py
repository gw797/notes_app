from data_base.data_base import Database
from repository.note_repository import NoteRepository
from models.base_note import BaseNote
from utils.note_logger import logger
from utils.note_types import NoteFactory


class NoteService:

    def __init__(self, repository: NoteRepository) -> None:
        self.repository = repository
        self.db: Database = repository.load()

    def get_all_notes(self) -> list[BaseNote]:
        return self.db.notes

    def get_note_by_id(self, note_id: int) -> BaseNote | None:
        for note in self.db.notes:
            if note.id == note_id:
                logger.info("Note %s found.", note_id)
                return note

        logger.warning("Note %s does not exist.", note_id)
        return None

    def _add_note(self, note: BaseNote) -> BaseNote:
        self.db.notes.append(note)
        self.repository.save(self.db)

        logger.info("Note %s created successfully.", note.id)

        return note

    def create(
            self,
            note_type: str,
            title: str,
            content: str
    ) -> BaseNote | None:

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

    def update_note(
            self,
            note_id: int,
            **kwargs
    ) -> BaseNote | None:

        note = self.get_note_by_id(note_id)

        if note is None:
            return None

        for field, value in kwargs.items():
            if value is not None:
                setattr(note, field, value)

        self.repository.save(self.db)

        logger.info("Note %s updated successfully.", note_id)

        return note

    def delete_note(self, note_id: int) -> None:
        self.repository.delete(self.db, note_id)

        logger.info("Note %s deleted successfully.", note_id)

