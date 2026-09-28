from datetime import datetime

from .base_note import BaseNote


class ListNote(BaseNote):

    def __init__(
            self,
            title: str,
            notes_list: list[str],
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

        self.notes_list = notes_list
#TODO
    @classmethod
    def from_dict(cls, data: dict) -> "ListNote":
        base_note_data = super().from_dict(data)
        return cls(
            **base_note_data,
            notes_list=data["notes_list"],
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["notes_list"] = self.notes_list
        return data
