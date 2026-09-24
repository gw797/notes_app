class Database:
    def __init__(self, notes:list, last_id:int =0):
        self.notes = notes or []
        self.last_id = last_id

    def get_next_id(self)-> int :
        self.last_id += 1
        return self.last_id


