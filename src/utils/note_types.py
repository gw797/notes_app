from models.list_note import ListNote
from models.simple_note import SimpleNote
from models.bookmark_note import BookmarkNote


class NoteFactory:
    NOTE_TYPES = {
        "simple": SimpleNote,
        "bookmark": BookmarkNote,
        "list": ListNote
    }

    @classmethod
    def create(cls, note_type, title, content, note_id):
        note_class = cls.NOTE_TYPES.get(note_type)

        if note_class is None:
            raise ValueError(f"Unknown note type: {note_type}")

        if note_type == "list":
            content = content.split(",")

        return note_class(
            title,
            content,
            note_id=note_id
        )

    @classmethod
    def from_dict(cls, data):
        note_class = {
            "SimpleNote": SimpleNote,
            "BookmarkNote": BookmarkNote,
            "ListNote": ListNote
        }.get(data["type"])

        if note_class is None:
            raise ValueError(f"Unknown note type: {data['type']}")

        return note_class.from_dict(data)