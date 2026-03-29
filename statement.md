# Problem Statement & Scope

## Project Overview
**Project Name:** MessMate - Hostel Mess Meal Optimizer
**Platform:** Command Line Interface (CLI)
**Language:** Python 3

**MessMate** is a targeted utility tool designed to solve a daily frustration for health-conscious hostel students. Hostel mess menus are often fixed, highly repetitive, and lack nutritional transparency. For students trying to achieve specific fitness goals—such as hitting daily protein targets, maintaining a calorie deficit, or avoiding excess carbohydrates—manually filtering daily meals is a tedious process. 

MessMate automates this by analyzing the daily unstructured mess menu and cross-referencing it with an internal nutritional knowledge base. It provides users with a quick, data-driven "Fitness & Macro Report" for any given meal, empowering them to make mindful and healthy dietary decisions effortlessly.

---

## Scope of the Project

### In-Scope (Current Version)
The current implementation of MessMate covers the core logic required for the BYOP course evaluation:
1. **Data Ingestion:** Capable of reading and parsing weekly mess schedules from a structured CSV file (`menu.csv`).
2. **Nutritional Mapping:** Matches menu items against a static Python dictionary containing approximate macros, calories, and health tags.
3. **Automated Calculation:** Computes the estimated total protein and total calories for the user's selected meal.
4. **Smart Flagging:** Identifies and warns users about high-carb or excessively oily/junk food items present in their meal.
5. **CLI Interaction:** Provides a clean, text-based terminal interface for user input and report generation.

### Out of Scope (Future Scope & Enhancements)
While the foundational logic is robust, the following features are outside the scope of the current CLI version but are planned for future updates:
1. **Personal User Profiles:** Saving individual user data (age, weight, goal calories) using file I/O or databases to provide percentage-based daily tracking.
2. **Graphical User Interface (GUI):** Transitioning from the terminal to a web-based dashboard using frameworks like Streamlit or Flask.
3. **Live API Integration:** Fetching exact, real-time nutritional data from third-party APIs (like Nutritionix) instead of relying on a static internal dictionary.
4. **Automated Weekly Meal Planning:** An algorithm to auto-suggest the best meals for the entire week based on a user's selected goal (e.g., "Fat Loss" vs. "Muscle Gain").
