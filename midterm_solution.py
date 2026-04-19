student_name = input("Student name: ")
weekly_budget = int(input("Weekly budget: "))
print()
print("=" * 50)
print("   WEEKLY EXPENSE -- CATEGORIES")
print("=" * 50)

expense_category = [
    ["1. Food & Drinks", "[e.g. Lunch, snacks, coffee]"],
    ["2. Transportation", "[e.g. Bus, jeepney, ride-share]"],
    ["3. Mobile / Internet", "[e.g. Load, data plan, WiFi top-up]"],
    ["4. School Supplies", "[e.g. Notebook, pen, bond paper]"],
    ["5. Entertainment", "[e.g. Games, movies, hangout]"],
]
for num in expense_category:
    print(f"{num[0]:<22} {num[1]}")

print("=" * 50)

categories = [] 
descriptions = []
amounts = []
total = 0
limit = weekly_budget * 0.25

print()

for i in range(4):
    print(f"--- EXPENSE {i+1} ---")
        
    while True:
        cat_num = int(input("Category (0 to skip): "))
        
        if cat_num == 0:
            break
        
        elif cat_num >=1 and cat_num <= 5:
            break
        else:
            print("Invalid category. Please try again.")
    
    if cat_num == 0:
        print()
        continue
    
    desc = input("Description: ")
    amount = int(input("Amount: "))
    
    categories.append(cat_num)
    descriptions.append(desc)
    amounts.append(amount)
