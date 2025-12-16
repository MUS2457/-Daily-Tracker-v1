🗓️ Daily Tracker (Python CLI)

A simple command-line Daily Tracker built with Python to record my daily activities (coding, gym, work, study, etc.), analyze time usage, and track mood trends.

This project focuses on clean logic, modular design, and real-world data handling, following good software practices while remaining beginner-friendly.

* Add Daily Data

Choose a task type (coding, gym, work, study)

Enter duration in minutes

Select mood (tired, okay, good)

Add an optional note

Add multiple entries in one session

📊 Automatic Analysis

Total time spent (minutes & hours)

Time spent per task

Most & least time-consuming tasks

Mood frequency

Average mood score

* Persistent Storage

Saves daily data with a timestamp in JSON format

Loads previously saved history safely

Prevents overwriting existing data

* Project Structure
DailyTracker/
│
├── main.py           # Menu & program flow
├── input_data.py     # User input & validation
├── calculation.py    # Analysis logic
├── storage.py        # Save / load JSON data
├── daily.json        # Stored data (auto-created)
└── README.md

▶️ How to Run
python main.py

📝 Example Output
--- Daily Summary ---
Total time spent: 180 minutes (3.00 hours)
Most time spent on : coding
Least time spent on: gym

Mood frequency:
 - good: 2
 - tired: 1

Average mood score: 2.33
Data saved successfully ✅

* Design Philosophy

Small, focused functions (single responsibility)

Functions return data instead of printing

Logic separated from UI (main.py)

Built step-by-step and improved version by version

Beginner-friendly but structured like real projects

* What This Project Practices

Lists & dictionaries (including nested data)

Loops & conditionals

Modular programming

Input validation

JSON file handling

Clean return-based logic
