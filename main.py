import csv

# 1. Nutrition Knowledge Base: Added 'calories' for better macro tracking!
nutrition_db = {
    "Boiled Egg": {"protein": 6, "calories": 78, "category": "High Protein/Low Carb"},
    "Chicken Dum Biryani": {"protein": 25, "calories": 450, "category": "High Protein"},
    "Butter Chicken": {"protein": 20, "calories": 350, "category": "High Protein/Low Carb"},
    "Paneer Butter Masala": {"protein": 12, "calories": 320, "category": "Good Protein"},
    "Matar Paneer Gravy": {"protein": 10, "calories": 280, "category": "Good Protein"},
    "Toor Dal": {"protein": 7, "calories": 150, "category": "Healthy Veg"},
    "Dal Tadka": {"protein": 8, "calories": 160, "category": "Healthy Veg"},
    "Dal Fry": {"protein": 8, "calories": 170, "category": "Healthy Veg"},
    "Masala Dal (Moong)": {"protein": 7, "calories": 140, "category": "Healthy Veg"},
    "Egg Chop Masala": {"protein": 12, "calories": 200, "category": "High Protein/Low Carb"},
    "Egg Bhurji": {"protein": 14, "calories": 220, "category": "High Protein/Low Carb"},
    "Samosa/Dal Kachori": {"protein": 4, "calories": 250, "category": "Oily/Junk"},
    "Vada Pav": {"protein": 3, "calories": 280, "category": "Oily/Junk"},
    "Bhatura/Chole (Dry)": {"protein": 6, "calories": 400, "category": "Oily/Junk"},
    "Aloo Paratha With Curd": {"protein": 6, "calories": 350, "category": "High Carb"},
    "White Rice": {"protein": 3, "calories": 130, "category": "High Carb"}
}

def get_meal_items(day, meal_type):
    """
    Reads the CSV file and retrieves menu items for a specific day and meal.
    """
    items = []
    try:
        with open('menu.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader) # Skip the header row
            for row in reader:
                # row[0] = Day, row[1] = Meal, row[2] = ItemName
                if row[0].strip().lower() == day.strip().lower() and row[1].strip().lower() == meal_type.strip().lower():
                    items.append(row[2].strip())
    except FileNotFoundError:
        print("❌ Error: 'menu.csv' file not found. Ensure both files are in the same directory.")
    
    return items

def analyze_meal(items):
    """
    Analyzes the meal items against the nutrition database and provides fitness recommendations.
    """
    total_protein = 0
    total_calories = 0
    warnings = []
    high_carb_warnings = []
    protein_rich_items = []

    print("\n🍽️ --- What's on Your Plate Today? --- 🍽️")
    for item in items:
        print(f"- {item}")
        
        # Check each item against our mock nutrition database
        for key in nutrition_db:
            if key.lower() in item.lower():
                protein = nutrition_db[key]["protein"]
                calories = nutrition_db[key]["calories"]
                category = nutrition_db[key]["category"]
                
                total_protein += protein
                total_calories += calories
                
                if protein >= 8:
                    protein_rich_items.append(f"{item} (~{protein}g protein)")
                if "Oily/Junk" in category:
                    warnings.append(item)
                if "High Carb" in category:
                    high_carb_warnings.append(item)

    # Final Output Display
    print("\n💪 --- FITNESS & MACRO REPORT --- 💪")
    print(f"🔥 Estimated Total Calories: ~{total_calories} kcal")
    print(f"🥩 Estimated Total Protein: ~{total_protein}g")
    
    if protein_rich_items:
        print("🟢 Best Protein Sources in this meal: ", ", ".join(protein_rich_items))
    else:
        print("🔴 Low Protein Alert! Consider adding extra eggs or a protein supplement.")

    if warnings:
        print("⚠️ JUNK FOOD ALERT: ", ", ".join(warnings))
        print("   -> Consume in moderation unless it's a cheat day.")
        
    if high_carb_warnings:
        print("🍞 HIGH CARB ALERT: ", ", ".join(high_carb_warnings))
        print("   -> If on a fat-loss/low-carb diet, monitor portion sizes for these items.")

def main():
    print("=====================================================")
    print("  MESSMATE - The Hostel Meal Optimizer (BYOP Project)")
    print("=====================================================")
    print("This program helps you make healthier choices based on your mess menu.\n")
    
    while True:
        day = input("Enter the day to check (e.g., Monday) [Or type 'exit' to quit]: ")
        if day.lower() == 'exit':
            print("Goodbye! Keep lifting and eating healthy! 💪✨")
            break
            
        meal = input("Enter the meal to check (Breakfast / Lunch / High Tea / Dinner): ")
        
        items = get_meal_items(day, meal)
        
        if items:
            analyze_meal(items)
        else:
            print("❌ Invalid input or no meal found for that day. Please check your spelling!")
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
