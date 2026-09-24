import json


class JsonStorage:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def load(self) -> dict:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            return data

        except FileNotFoundError:
            return {
                "last_id": 0,
                "notes": []
            }

    def save(self, data: dict) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

