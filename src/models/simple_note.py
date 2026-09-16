from datetime import datetime

from .base_note import BaseNote


class SimpleNote(BaseNote):

    def __init__(self, title, content, note_id, created_at=None):
        super().__init__(
            title=title,
            note_id=note_id,
            created_at=created_at
        )

        self.content = content

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            content=data["content"],
            note_id=data["id"],
            created_at=datetime.fromisoformat(data["created_at"])
            )