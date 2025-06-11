from personal_assistant.storage import Storage

class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
        }

    @staticmethod
    def from_dict(data):
        return Note(
            title=data['title'],
            content=data['content'],
            tags=data.get('tags', []),
        )

class NoteBook:
    def __init__(self):
        self.storage = Storage('notes.json')
        self.notes = self.load_notes()

    def load_notes(self):
        data = self.storage.load_data()
        return {title: Note.from_dict(info) for title, info in data.items()}

    def save_notes(self):
        data = {title: note.to_dict() for title, note in self.notes.items()}
        self.storage.save_data(data)

    def add_note(self, note):
        self.notes[note.title] = note
        self.save_notes()
        print(f"Note '{note.title}' add.")

    def search_notes(self, query):
        results = []
        for note in self.notes.values():
            if query.lower() in note.content.lower() or query.lower() in note.title.lower():
                results.append(note)
        return results

    def search_by_tags(self, tags):
        results = []
        for note in self.notes.values():
            if set(tags).issubset(set(note.tags)):
                results.append(note)
        return results

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            self.save_notes()
            print(f"Note '{title}' delete.")
        else:
            print(f"Note '{title}' not found.")

    def edit_note(self, title, content=None, tags=None):
        if title in self.notes:
            note = self.notes[title]
            if content:
                note.content = content
            if tags is not None:
                note.tags = tags
            self.save_notes()
            print(f"Note '{title}' updated.")
        else:
            print(f"Note '{title}' not found.")
