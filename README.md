# 🧠 Hackathon II – Phase I  
## **Evolution of Todo: Spec-Driven CLI Application**

This project is the **first step** in the Evolution of Todo journey, where software is built using **Spec-Driven Development** instead of manual coding.

In this phase, we created a **Python-based command-line Todo application** generated through **Claude Code** using structured specifications 📜🤖

---

## 🎯 Phase I

Build a fully functional **in-memory Todo CLI app** using:

- 🐍 Python  
- 🤖 Claude Code  
- 📘 Spec-Kit Plus  

All features were implemented by writing **Specs and Constitutions**, then refining them until Claude Code generated the correct implementation.

## ✨ Features

This CLI app allows users to manage daily tasks with the following functionality:

- ➕ **Add Task** – Create a new todo with title and optional description  
- 📋 **View Tasks** – See all tasks with ID and completion status  
- ✏️ **Update Task** – Modify title and/or description  
- ❌ **Delete Task** – Remove a task by ID  
- ✅ **Mark Complete / Incomplete** – Toggle task status  

All data is stored **in memory** for this phase.

---

## 🖥️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13+ | Core programming language |
| Claude Code | AI code generation from specs |
| Spec-Kit Plus | Spec-driven development framework |

---

## 📂 Project Structure

src/
│
├── models.py # Task data model
├── services.py # Business logic for task operations
├── cli.py # Command-line interface handling
├── utils.py # Helper and utility functions
└── main.py # Application entry point

---

## ▶️ How to Run

1️⃣ Make sure Python 3.13+ is installed  
2️⃣ Navigate to the project directory  
3️⃣ Run the application:

```bash
python src/main.py

