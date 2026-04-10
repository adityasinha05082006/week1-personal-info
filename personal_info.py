# Name: Your Name
# Project: Personal Information Manager
# Description: This program stores and displays personal information using variables, input, and formatting.


# -------------------------------
# Step 1: Welcome Message
# -------------------------------

print("===================================")
print("   Welcome to Personal Info Manager")
print("===================================\n")

# -------------------------------
# Step 2: User Input with Validation
# -------------------------------


# Name
name = input("Enter your name: ").strip()
while name == "":
    print("❌ Name cannot be empty.")
    name = input("Enter your name: ").strip()

# Age
age_input = input("Enter your age: ").strip()
while not age_input.isdigit():
    print("❌ Please enter a valid number.")
    age_input = input("Enter your age: ").strip()
age = int(age_input)

# City
city = input("Enter your city: ").strip()
while city == "":
    print("❌ City cannot be empty.")
    city = input("Enter your city: ").strip()

# Hobby
hobby = input("Enter your hobby: ").strip()
while hobby == "":
    print("❌ Hobby cannot be empty.")
    hobby = input("Enter your hobby: ").strip()

# Favorite Food
fav_food = input("Enter your favorite food: ").strip()
while fav_food == "":
    print("❌ Input cannot be empty.")
    fav_food = input("Enter your favorite food: ").strip()

# Favorite Color
fav_color = input("Enter your favorite color: ").strip()
while fav_color == "":
    print("❌ Input cannot be empty.")
    fav_color = input("Enter your favorite color: ").strip()

# -------------------------------
# Step 3: Processing
# -------------------------------

age_in_months = age * 12   # Convert age to months

# -------------------------------
# Step 4: Display Output
# -------------------------------

print("\n===================================")
print("        PERSONAL INFORMATION        ")
print("===================================")

print(f"👤 Name            : {name.title()}")
print(f"🎂 Age             : {age} years")
print(f"📅 Age in Months   : {age_in_months} months")
print(f"🏙️ City           : {city.title()}")
print(f"🎯 Hobby          : {hobby.capitalize()}")

print("\n---------- Favorites ----------")
print(f"🍕 Favorite Food  : {fav_food.capitalize()}")
print(f"🎨 Favorite Color : {fav_color.capitalize()}")

print("===================================")

# -------------------------------
# Step 5: Goodbye Message
# -------------------------------

print("\n✨ Thank you for using the program!")
print("👋 Goodbye!\n")