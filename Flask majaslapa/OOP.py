from website.models import Note, User

# learn python abstractclass
class IObjectModel:
    def func():
        pass

class NoteModel(IObjectModel):
    def __init__(self, note_data: Note):
        self.note_data = note_data

    def do_something_with_note(self): 
        self.note_data.data = 0

class UserModel(IObjectModel):
    pass

# learn incapsulation in python, implement it for self.note_data
