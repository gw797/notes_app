from datetime import datetime

from .base_note import BaseNote


class BookmarkNote(BaseNote):

    def __init__(
            self,
            title: str,
            url: str,
            note_id: int,
            created_at: datetime | None = None
    ) -> None:
        super().__init__(
            title=title,
            note_id=note_id,
            created_at=created_at
        )

        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "BookmarkNote":
        fields = BaseNote.get_common_fields(data)

        return cls(
            title=fields["title"],
            note_id=fields["note_id"],
            created_at=fields["created_at"],
            url=data["url"]
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["url"] = self.url

        return data