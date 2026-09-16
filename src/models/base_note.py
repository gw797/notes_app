from datetime import datetime, timezone


class BaseNote:

    def __init__(self, title, note_id, created_at=None):
        self.id = note_id
        self.title = title
        self.created_at = created_at or datetime.now(timezone.utc)

    def to_dict(self):
        data = self.__dict__.copy()
        data["type"] = self.__class__.__name__
        data["created_at"] = self.created_at.isoformat()

        return data


    def __str__(self):
        return str(self.__dict__)