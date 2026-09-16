class Database:
    def __init__(self, notes=None, last_id=0):
        self.notes = notes or []
        self.last_id = last_id

    def get_next_id(self):
        self.last_id += 1
        return self.last_id


