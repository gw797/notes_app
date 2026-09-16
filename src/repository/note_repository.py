from select import select
from sqlalchemy.orm import Session

from src.models.note import Note


class NoteRepository:

    def __init__(self, session: Session):
        self.session = session

    def save (self, note: Note):
        self.session.add(note)
        self.session.commit()
        return note

    def get_by_id(self, note_id):
        return self.session.get(Note, note_id)

    def get_all(self):
        statement = select(Note)
        return self.session.scalars(statement).all()

    def update(self, note):
        self.session.commit()
        return note

    def delete(self, note_id):
        note = self.session.get(Note, note_id)

        if note is None:
            return None

        self.session.delete(note)
        self.session.commit()

        return note
