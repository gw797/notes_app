from datetime import datetime

from .base_note import BaseNote


class BookmarkNote(BaseNote):

    def __init__(self, title:str, url:str, note_id:int, created_at:datetime=None) -> None:
        super().__init__(
            title=title,
            note_id=note_id,
            created_at=created_at
        )

        self.url = url

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            url=data["url"],
            note_id=data["id"],
            created_at=datetime.fromisoformat(data["created_at"])
        )