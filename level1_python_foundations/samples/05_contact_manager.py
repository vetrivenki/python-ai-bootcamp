# 05_contact_manager.py
# Level 1 — Topic 5: File I/O (CSV, JSON, TXT) + pathlib

import json
import csv
from pathlib import Path

CONTACTS_FILE = Path("contacts.json")


def load_contacts():
    if CONTACTS_FILE.exists():
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)


def add_contact(name: str, phone: str, email: str):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Added: {name}")


def export_to_csv(filename="contacts.csv"):
    contacts = load_contacts()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email"])
        writer.writeheader()
        writer.writerows(contacts)
    print(f"Exported to {filename}")


def show_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts yet.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


if __name__ == "__main__":
    add_contact("Alice", "123-456-7890", "alice@email.com")
    add_contact("Bob", "987-654-3210", "bob@email.com")
    show_contacts()
    export_to_csv()
