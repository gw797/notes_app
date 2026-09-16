from datetime import datetime

from .base_note import BaseNote


class ListNote(BaseNote):

    def __init__(self, title, notes_list, note_id, created_at=None):
        super().__init__(
            title=title,
            note_id=note_id,
            created_at=created_at
        )

        self.notes_list = notes_list

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            notes_list=data["notes_list"],
            note_id=data["id"],
            created_at=datetime.fromisoformat(data["created_at"])
        )