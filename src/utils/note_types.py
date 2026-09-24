from models.base_note import BaseNote
from models.list_note import ListNote
from models.simple_note import SimpleNote
from models.bookmark_note import BookmarkNote


class NoteFactory:

    NOTE_TYPES = {
        "SimpleNote": SimpleNote,
        "BookmarkNote": BookmarkNote,
        "ListNote": ListNote
    }

    @classmethod
    def create(
            cls,
            note_type: str,
            title: str,
            content: str,
            note_id: int
    ) -> BaseNote:

        note_class = cls.NOTE_TYPES.get(note_type)

        if note_class is None:
            raise ValueError(f"Unknown note type: {note_type}")

        if note_type == "ListNote":
            content = content.split(",")

        return note_class(
            title,
            content,
            note_id=note_id
        )

    @classmethod
    def from_dict(cls, data: dict) -> BaseNote:
        note_class = cls.NOTE_TYPES.get(data["type"])

        if note_class is None:
            raise ValueError(f"Unknown note type: {data['type']}")

        return note_class.from_dict(data)
