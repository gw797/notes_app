from src.models.list import ListNote
from src.models.simple import SimpleNote
from src.models.bookmark import BookmarkNote


class NoteFactory:
    NOTE_TYPES = {
        "simple": SimpleNote,
        "bookmark": BookmarkNote,
        "list": ListNote
    }

    @classmethod
    def create(cls, note_type, title, content):
        note_class = cls.NOTE_TYPES.get(note_type)

        if note_class is None:
            raise ValueError(f"Unknown note type: {note_type}")


        return note_class(
           title=  title,
           content= content,
        )

