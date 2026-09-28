from datetime import datetime

from .base_note import BaseNote


class BookmarkNote(BaseNote):

    def __init__(
            self,
            title: str,
            url: str,
            note_id: int,
            created_at: datetime | None = None,
            updated_at: datetime | None = None
    ) -> None:
        super().__init__(
            title=title,
            note_id=note_id,
            created_at=created_at,
            updated_at=updated_at
        )

        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "BookmarkNote":
        base_note_data = super().from_dict(data)
        return cls(
            **base_note_data,
            url=data["url"]
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["url"] = self.url

        return data