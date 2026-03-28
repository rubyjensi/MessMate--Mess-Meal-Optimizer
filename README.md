# MessMate: Hostel Mess Meal Optimizer

## Project Overview
**MessMate** is a Python-based Command Line Interface (CLI) tool designed to help hostel students make healthier, fitness-oriented food choices. It analyzes the daily, unstructured hostel mess menu and cross-references it with a nutritional knowledge base to provide actionable dietary insights, including protein and calorie tracking.

## Problem Statement (BYOP Concept)
Hostel students, especially those following specific fitness routines (like hitting daily protein goals or maintaining a calorie deficit), often struggle to filter out what to eat from a fixed, highly repetitive mess menu. Manually checking the menu and guessing the nutritional value daily is tedious and leads to poor dietary choices.

## The Solution
MessMate reads the weekly mess menu from a structured dataset (`menu.csv`) and matches the meal items against a predefined Python dictionary containing approximate nutritional categories (Protein, Calories, Carbs, Fats, Junk). It then outputs a "Fitness & Macro Report" for any specific day and meal, calculating estimated total calories, highlighting high-protein sources, and flagging oily/high-carb foods.

## Features
- **Automated Calorie & Macro Tracking:** Calculates estimated total calories and protein for the selected meal.
- **Data File Handling:** Dynamically reads menu data using Python's `csv` module.
- **Nutritional Logic:** Uses a dictionary-based knowledge base to categorize food items.
- **Smart Alerts:** Warns users about high-carb or oily food items based on their selection.
- **Terminal Executable:** Runs entirely cleanly in the terminal without needing any GUI setup.

---

## How to Run the Project (Execution Steps)

**Prerequisites:** You only need **Python 3.x** installed on your system. No external heavy libraries are required.

**Step 1: Clone the Repository**
Download or clone this repository to your local machine.
`git clone https://github.com/rubyjensi/MessMate--Mess-Meal-Optimizer.git`

**Step 2: Navigate to the Directory**
Open your terminal or command prompt and go to the folder where the files are saved.
`cd MessMate--Mess-Meal-Optimizer`

**Step 3: Run the Program**
Execute the main Python script.
`python main.py`

**Step 4: Interact with the CLI**
- The program will ask: `Enter the day to check (e.g., Monday)`
- Then it will ask: `Enter the meal to check (Breakfast / Lunch / High Tea / Dinner)`
- View your personalized macro and calorie report! Type `exit` to close the program.

---

## Concepts & Technologies Used
- **Language:** Python 3
- **Data Structures:** Lists, Dictionaries (for fast macro/calorie lookups), Strings.
- **Control Flow:** `if/else` conditionals, `while` loops, `for` loops.
- **File I/O:** Reading CSV files using `with open()`.
- **Exception Handling:** `try/except` blocks to prevent crashes if the database is missing.

## Future Scope & Enhancements
The current version of MessMate successfully demonstrates the application of Python fundamentals to solve a real-world problem. However, the project architecture allows for several advanced future enhancements:
* **Personalized User Profiles:** Implementing file-handling to save individual user profiles with specific daily macronutrient (protein/carbs/fats) and calorie targets.
* **Web/GUI Transition:** Upgrading from a Command Line Interface (CLI) to a graphical web interface using Python libraries like Streamlit for a more intuitive user experience.
* **Third-Party API Integration:** Instead of relying on a static dictionary, the program could dynamically fetch live, scientifically accurate nutritional data using external APIs like Nutritionix.
* **Weekly Diet Automation:** Developing an algorithm that auto-selects the optimal meals for the entire week from the CSV file and generates a personalized diet chart based on the user's fitness goals (e.g., Fat Loss vs. Muscle Gain).
