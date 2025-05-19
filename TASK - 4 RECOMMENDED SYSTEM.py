# Simple Recommendation System using Content-Based Filtering

# Sample data for movies, books, and products
items = {
    "movies": [
        {"title": "Dilwale", "actor": "shahrukh khan", "language": "Hindi"},
        {"title": "War", "actor": "Hrithik Roshan", "language": "Hindi"},
        {"title": "Bhool Bhulaiyaa 2", "actor": "Karthik Aaryan", "language": "Hindi"},
        {"title": "Bhediya", "actor": "Varun Dhawan", "language": "Hindi"},
        {"title": "Pushpa", "actor": "allu arjun", "language": "South"},
        {"title": "Arjun Reddy", "actor": "vijay deverakonda", "language": "South"},
        {"title": "Jersey", "actor": "nani", "language": "South"},
        {"title": "Acharya", "actor": "chiranjeevi", "language": "South"},
        {"title": "Manam", "actor": "nagarjuna", "language": "South"},
        {"title": "Bolo Na Tumi Amar", "actor": "dev", "language": "Bengali"},
        {"title": "Boss", "actor": "Jeet", "language": "Bengali"},
        {"title": "Ami Sudhu Cheyechi Tomay", "actor": "bonny", "language": "Bengali"}
    ],
    "books": [
        "Wings of Fire by A.P.J. Abdul Kalam",
        "The Alchemist by Paulo Coelho",
        "2 States by Chetan Bhagat",
        "Sita by Amish Tripathi",
        "The Monk Who Sold His Ferrari by Robin Sharma"
    ],
    "products": [
        "Wireless Earbuds",
        "Fitness Band",
        "Bluetooth Speaker",
        "Smartphone",
        "Laptop Bag"
    ]
}

# Function to recommend movies based on preferred actor
def recommend_movies_by_actor(preferred_actor):
    print(f"\n--- Recommended Movies for Actor: {preferred_actor.title()} ---")
    found = False
    for movie in items["movies"]:
        if movie["actor"].lower() == preferred_actor.lower():  # case-insensitive match
            print(f"{movie['title']} ({movie['language']})")
            found = True
    if not found:
        print("No movies found for this actor.")

# Function to recommend random books
def recommend_books():
    print("\n--- Recommended Books ---")
    for book in items["books"]:
        print(f"- {book}")

# Function to recommend random products
def recommend_products():
    print("\n--- Recommended Products ---")
    for product in items["products"]:
        print(f"- {product}")

# Main function to interact with user
def main():
    print("Welcome to the Simple Recommendation System!")
    print("Please tell us your preferences to get personalized recommendations.")

    # Taking user's preferred actor as input
    actor = input("Enter your favorite actor's name (Hindi/South/Bengali): ")

    # Calling movie recommendation
    recommend_movies_by_actor(actor)

    # Calling book recommendation
    recommend_books()

    # Calling product recommendation
    recommend_products()


main()