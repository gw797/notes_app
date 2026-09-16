class NoteService:

    def __init__(self, repository):
        self.repository = repository

    def get_note(self, note_id):
        return self.repository.get_by_id(note_id)

    def get_all_notes(self):
        return self.repository.get_all()

    def create_note(self, note):
        return self.repository.save(note)

    def update_note(self, note_id, **kwargs):
        note = self.get_note(note_id)
        for key, value in kwargs.items():
            setattr(note, key, value)
            self.repository.update(note)

    def delete_note(self, note_id):
        return self.repository.delete(note_id)






