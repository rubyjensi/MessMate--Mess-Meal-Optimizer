# MessMate: Hostel Mess Meal Optimizer

## Project Overview
**MessMate** is a Python-based Command Line Interface (CLI) tool designed to help hostel students make healthier, fitness-oriented food choices. It analyzes the daily, unstructured hostel mess menu and cross-references it with a nutritional knowledge base to provide actionable dietary insights.

## Problem Statement (BYOP Concept)
Hostel students, especially those following specific fitness routines (like gym-goers focusing on high-protein or low-carb diets), often struggle to filter out what to eat from a fixed, highly repetitive mess menu. Manually checking the menu and guessing the nutritional value daily is tedious.

## The Solution
MessMate reads the weekly mess menu from a structured dataset (`menu.csv`) and matches the meal items against a predefined Python dictionary containing approximate nutritional categories (Protein, Carbs, Fats, Junk). It then outputs a "Fitness & Macro Report" for any specific day and meal, highlighting high-protein sources and flagging oily/high-carb foods.

## Features
- **Data File Handling:** Dynamically reads menu data using Python's `csv` module.
- **Nutritional Logic:** Uses a dictionary-based knowledge base to categorize food items.
- **Smart Alerts:** Warns users about high-carb or oily food items based on their selection.
- **Terminal Executable:** Runs entirely cleanly in the terminal without needing any GUI setup.

---

## How to Run the Project (Execution Steps)

**Prerequisites:** You only need **Python 3.x** installed on your system. No external heavy libraries are required.

**Step 1: Clone the Repository**
Download or clone this repository to your local machine.
`git clone <your-repository-url>`

**Step 2: Navigate to the Directory**
Open your terminal or command prompt and go to the folder where the files are saved.
`cd MessMate--Mess-Meal-Optimizer`

**Step 3: Run the Program**
Execute the main Python script.
`python main.py`

**Step 4: Interact with the CLI**
- The program will ask: `Enter the day to check (e.g., Monday)`
- Then it will ask: `Enter the meal to check (Breakfast / Lunch / High Tea / Dinner)`
- View your personalized macro report! Type `exit` to close the program.

---

## Concepts & Technologies Used
- **Language:** Python 3
- **Data Structures:** Lists, Dictionaries (for fast macro lookups), Strings.
- **Control Flow:** `if/else` conditionals, `while` loops, `for` loops.
- **File I/O:** Reading CSV files using `with open()`.
- **Exception Handling:** `try/except` blocks to prevent crashes if the database is missing.
