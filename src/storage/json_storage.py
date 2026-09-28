import json


class JsonStorage:

    def __init__(self, filename: str) -> None:
        self.filename:str=filename
    def load(self) -> dict:

            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            return data



    def save(self, data: dict) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

