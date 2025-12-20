# OOP-Based Todo App (CLI)

This project is a command-line Todo application built using Python and Object-Oriented Programming principles.
It uses local JSON storage to persist tasks without using a database.

## Features
- Add Todo
- View Todos
- Update Todo
- Delete Todo
- Persistent JSON storage

## JSON Serialization
Task objects are converted to dictionaries before saving to JSON.
When the app starts, JSON data is converted back into Task objects.

## Run the Project
```bash
python main.py
