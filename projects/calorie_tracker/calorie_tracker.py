import json

PRODUCTS_FILE = "products.json"
DAILY_LOG_FILE = "daily_log.json"

def load_products():
    try:
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Error reading products file. Starting with empty list.")
        return []

def save_products(products):
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4)

def load_daily_logs():
    try:
        with open(DAILY_LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Error reading daily logs file. Starting with empty list.")
        return []

def save_daily_logs(daily_logs):
    with open(DAILY_LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(daily_logs, f, indent=4)

class Food:
    def __init__(self, name, calories, fat, carbohydrates, proteins):
        self.name = name
        self.calories = calories
        self.fat = fat
        self.carbohydrates = carbohydrates 
        self.proteins = proteins
        
    def to_dict(self):
        return {
            "name": self.name,
            "calories": self.calories,
            "fat": self.fat,
            "carbohydrates": self.carbohydrates,
            "proteins": self.proteins,
        }

class DailyLog:
    def __init__(self, date, calories_consumed, fat_consumed, carbs_consumed, protein_consumed, products):
        self.date = date
        self.calories_consumed = calories_consumed
        self.fat_consumed = fat_consumed
        self.carbs_consumed = carbs_consumed 
        self.protein_consumed = protein_consumed
        self.products = products
    
    def to_dict(self):
        return {
            "date": self.date,
            "calories_consumed": self.calories_consumed,
            "fat_consumed": self.fat_consumed,
            "carbs_consumed": self.carbs_consumed,
            "protein_consumed": self.protein_consumed,
            "products": self.products,
        }

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def add_new_food():
    name = input("Enter food name: ").strip()
    if not name:
        print("❌ Food name cannot be empty.")
        return
        
    calories = get_float_input("Enter calories per serving (100g): ")
    fat = get_float_input("Enter fat per serving (100g): ")
    carbohydrates = get_float_input("Enter carbohydrates per serving (100g): ")
    proteins = get_float_input("Enter proteins per serving (100g): ")
    
    products = load_products()
    new_food = Food(name, calories, fat, carbohydrates, proteins).to_dict()
    products.append(new_food)
    save_products(products)
    print(f"✅ {name} added successfully!")

def log_food_intake():
    daily_logs = load_daily_logs()
    products = load_products()

    date = input("Enter date (YYYY-MM-DD): ").strip()
    while not date:  # Simple validation
        print("❌ Date cannot be empty.")
        date = input("Enter date (YYYY-MM-DD): ").strip()

    total_calories = 0
    total_fat = 0
    total_carbs = 0
    total_protein = 0
    eaten_products = []

    while True:
        product_name = input("Enter product name (or 'done' to finish): ").strip()
        if product_name.lower() == 'done':
            break

        # Try to find product in database
        product = next((p for p in products if p["name"].lower() == product_name.lower()), None)

        if not product:
            print(f"❌ Product '{product_name}' not found in database.")
            choice = input("Would you like to add it now? (yes/no): ").strip().lower()
            if choice == 'yes':
                # Add new product to database
                print(f"\nAdding new product: {product_name}")
                calories = get_float_input("Enter calories per serving (100g): ")
                fat = get_float_input("Enter fat per serving (100g): ")
                carbs = get_float_input("Enter carbohydrates per serving (100g): ")
                protein = get_float_input("Enter proteins per serving (100g): ")
                
                new_product = {
                    "name": product_name,
                    "calories": calories,
                    "fat": fat,
                    "carbohydrates": carbs,
                    "proteins": protein
                }
                products.append(new_product)
                save_products(products)
                print(f"✅ {product_name} added to database!")
                product = new_product
            else:
                print("Skipping this product.")
                continue

        # Get amount consumed
        grams = get_float_input(f"Enter amount of {product['name']} eaten (grams): ")
        while grams <= 0:
            print("❌ Grams must be positive.")
            grams = get_float_input(f"Enter amount of {product['name']} eaten (grams): ")

        # Calculate nutritional values
        factor = grams / 100
        total_calories += product["calories"] * factor
        total_fat += product["fat"] * factor
        total_carbs += product["carbohydrates"] * factor
        total_protein += product["proteins"] * factor

        eaten_products.append({
            "name": product["name"],
            "grams": grams
        })

    if not eaten_products:
        print("❌ No products were logged.")
        return

    # Check if log exists for date
    existing_log = next((log for log in daily_logs if log["date"] == date), None)

    if existing_log:
        print(f"⚠️ A log for {date} already exists.")
        choice = input("Would you like to update it? (yes/no): ").strip().lower()
        if choice == "yes":
            existing_log["calories_consumed"] += total_calories
            existing_log["fat_consumed"] += total_fat
            existing_log["carbs_consumed"] += total_carbs
            existing_log["protein_consumed"] += total_protein
            existing_log["products"].extend(eaten_products)
            print(f"✅ Log for {date} updated successfully!")
        else:
            print("❌ No changes made.")
    else:
        new_log = {
            "date": date,
            "calories_consumed": total_calories,
            "fat_consumed": total_fat,
            "carbs_consumed": total_carbs,
            "protein_consumed": total_protein,
            "products": eaten_products
        }
        daily_logs.append(new_log)
        print(f"✅ New log for {date} added successfully!")

    save_daily_logs(daily_logs)

def view_daily_log():
    daily_logs = load_daily_logs()
    if not daily_logs:
        print("⚠️ No daily logs found. Please log some food first.")
        return

    date = input("Enter date (YYYY-MM-DD) to view log: ").strip()
    
    log = next((entry for entry in daily_logs if entry["date"] == date), None)

    if log:
        print(f"\n📅 Daily Log for {date}:")
        print(f"🔥 Calories: {log['calories_consumed']:.2f} kcal")
        print(f"🥩 Protein: {log['protein_consumed']:.2f} g")
        print(f"🥑 Fat: {log['fat_consumed']:.2f} g")
        print(f"🍞 Carbohydrates: {log['carbs_consumed']:.2f} g")

        print("\n🍽️ Foods Consumed:")
        for item in log.get("products", []):
            print(f"- {item.get('name', 'Unknown')} ({item.get('grams', 0):.2f}g)")
    else:
        print(f"❌ No log found for {date}.")

def main():
    while True:
        print("\nMain Menu:")
        action = input("Choose an option: (1) Add new product  (2) Log food intake  (3) View daily log  (4) Exit: ").strip()

        if action == "1":
            add_new_food()
        elif action == "2":
            log_food_intake()
        elif action == "3":
            view_daily_log()
        elif action == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()