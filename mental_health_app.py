import json
from datetime import datetime

class Journal:
    def __init__(self, filename='journal.json'):
        self.filename = filename
        self.entries = self._load()

    def _load(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError):
            return []

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.entries, f, indent=2)

    def add_entry(self, text):
        self.entries.append({'text': text, 'timestamp': datetime.now().isoformat()})
        self._save()

    def edit_entry(self, index, text):
        if 0 <= index < len(self.entries):
            self.entries[index]['text'] = text
            self.entries[index]['timestamp'] = datetime.now().isoformat()
            self._save()

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            self._save()

    def list_entries(self):
        return self.entries


def show_journal(journal):
    while True:
        print("\nJournal")
        print("1) View entries")
        print("2) Add entry")
        print("3) Edit entry")
        print("4) Delete entry")
        print("5) Back")
        choice = input("Select: ")
        if choice == '1':
            for i, entry in enumerate(journal.list_entries()):
                print(f"{i}: {entry['timestamp']} - {entry['text']}")
        elif choice == '2':
            text = input("Write your entry: ")
            journal.add_entry(text)
        elif choice == '3':
            idx = int(input("Entry number to edit: "))
            if 0 <= idx < len(journal.entries):
                new_text = input("New text: ")
                journal.edit_entry(idx, new_text)
            else:
                print("Invalid index")
        elif choice == '4':
            idx = int(input("Entry number to delete: "))
            journal.delete_entry(idx)
        elif choice == '5':
            break
        else:
            print("Invalid choice")


def show_toolkit():
    print("\nMental Health Toolkit")
    exercises = [
        "Take a deep breath and exhale slowly",
        "Write down three things you are grateful for",
        "Go for a short walk or stretch"
    ]
    for ex in exercises:
        print(f"- {ex}")
    input("Press Enter to return...")


def show_resources():
    print("\nResources")
    print("If you are in crisis, consider reaching out to a helpline:")
    print(" - National Suicide Prevention Lifeline (US): 988")
    print(" - Crisis Text Line: Text HOME to 741741")
    print(" - International hotlines: https://findahelpline.com/")
    input("Press Enter to return...")


def main():
    journal = Journal()
    while True:
        print("\nMain Menu")
        print("1) Journal")
        print("2) Toolkit")
        print("3) Resources")
        print("4) Quit")
        choice = input("Select: ")
        if choice == '1':
            show_journal(journal)
        elif choice == '2':
            show_toolkit()
        elif choice == '3':
            show_resources()
        elif choice == '4':
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
