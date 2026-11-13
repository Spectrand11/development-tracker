# Personal Development Tracker

A small command-line app for logging and managing personal development activities — learning goals, projects, habits, and their status.

Built as a learning project, so the code favors readability over cleverness.

## Features

- Add an activity (title, category, description, date)
- View all logged activities
- Search by keyword across title, category, and description
- Update a single field of an activity
- Delete an activity (with confirmation)
- Two summary views in progress (menu items 6 and 7 — not implemented yet)

## Requirements

- Python 3.8+

No third-party dependencies.

## Usage

```bash
python main.py
```

You'll get a numbered menu:

```
=============================
PERSONAL DEVELOPMENT TRACKER
=============================
1. Add an activity
2. View all activities
...
8. Exit
```

Enter a number, then follow the prompts.

## Project structure

```
development_tracker/
├── main.py        # CLI entry point, menu loop
├── tracker.py     # Tracker class: add/view/search/update/delete
├── activity.py    # Activity model
├── storage.py     # Persistence layer (placeholder)
└── .gitignore
```

`tracker.track` is a module-level singleton, which is what `main.py` drives.

## Status and limitations

- **Data is in-memory only.** Activities are lost when the program exits — `storage.py` and `activities.json` are placeholders for future persistence.
- Menu options **6 (progress summary)** and **7 (category summary)** are listed but not wired up.
- No tests yet.
