from datetime import datetime

from .base_note import BaseNote


class SimpleNote(BaseNote):

    def __init__(
            self,
            title: str,
            content: str,
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

        self.content = content

    @classmethod
    def from_dict(cls, data: dict) -> "SimpleNote":
        base_note_data = super().from_dict(data)
        return cls(
            **base_note_data,
            content=data["content"],
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["content"] = self.content
        return data
