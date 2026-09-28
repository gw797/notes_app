from datetime import datetime, timezone


class BaseNote:

    def __init__(
            self,
            title: str,
            note_id: int,
            created_at: datetime | None = None,
            updated_at: datetime | None = None
    ) -> None:
        self.id = note_id
        self.title = title
        self.created_at = created_at or datetime.now(timezone.utc)
        self.updated_at = updated_at or datetime.now(timezone.utc)


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "type": self.__class__.__name__
        }

    @classmethod
    def from_dict(cls, data: dict) -> dict:
        return {
            "title": data["title"],
            "note_id": data["id"],
            "created_at": datetime.fromisoformat(data["created_at"]),
             "updated_at": datetime.fromisoformat(
            data.get("updated_at", data["created_at"]))

        }

    def __str__(self) -> str:
        return (
            f"id = {self.id}, "
            f"title = {self.title}, "
            f"created_at = {self.created_at.strftime('%d/%m/%Y %H:%M')}"
            f"updated_at = {self.updated_at.strftime('%d/%m/%Y %H:%M')}"
        )