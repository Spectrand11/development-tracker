# Personal Development Tracker

A small command-line app for logging and managing personal development activities — learning goals, projects, and practice habits — along with quick progress and category summaries.

Built as a learning project, so the code favors readability over cleverness.

## Features

- Add an activity (title, category, description, date, status)
- View all logged activities
- Search by keyword across title, category, and description
- Update a single field of an activity (title, category, description, date, or status)
- Delete an activity (with confirmation)
- Progress summary (counts by status: Completed, In Progress, Not Started)
- Category summary (counts by category: Learning, Project, Practice)

Categories are `Learning`, `Project`, and `Practice`. Statuses are `Not Started`, `In Progress`, and `Completed`; newly added activities start as `Not Started`. Dates must use the `YYYY-MM-DD` format.

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
3. Search activities
4. Update activity
5. Delete activity
6. Progress summary
7. Category summary
8. Exit
```

Enter a number, then follow the prompts.

## Project structure

```
development_tracker/
├── main.py         # CLI entry point, menu loop and input validation
├── tracker.py      # Tracker class: add/view/search/update/delete/summaries
├── activity.py     # Activity model
├── storage.py      # Persistence layer (placeholder)
├── activities.json # Local data file (placeholder, git-ignored)
├── .gitignore
└── README.md
```

`tracker.track` is a module-level singleton, which is what `main.py` drives.

## Status and limitations

- **Data is in-memory only.** Activities are lost when the program exits — `storage.py` and `activities.json` are placeholders for future persistence.
- No tests yet.
