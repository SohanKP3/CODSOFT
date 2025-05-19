import random # Import the 'random' module for random selection

def curious_buddy(user_input): # Define a function named 'curious_companion' that takes user input
    user_input_lower = user_input.lower() # Convert the user's input to lowercase for case-insensitive matching

    greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"] # List of common greeting phrases
    farewells = ["bye", "goodbye", "see you later", "farewell", "take care"] # List of common farewell phrases
    thanks = ["thank you", "thanks", "appreciate it"] # List of phrases expressing gratitude
    weather_queries = ["weather like", "temperature in", "is it raining", "forecast for"] # List of phrases related to weather inquiries
    joke_queries = ["tell me a joke", "make me laugh", "a funny story"] # List of phrases asking for a joke
    fact_queries = ["tell me something interesting", "did you know", "learn something new"] # List of phrases asking for a fact
    hobby_queries = ["your hobbies", "what do you like to do", "any interests"] # List of phrases asking about the chatbot's hobbies
    help_queries = ["help", "what can you do", "how does this work"] # List of phrases asking for help or capabilities
    name_queries = ["what's your name", "who are you"] # List of phrases asking for the chatbot's name
    feeling_queries = ["how are you", "how's it going", "you doing"] # List of phrases asking about the chatbot's well-being

    if any(greeting in user_input_lower for greeting in greetings): # Check if any greeting word is present in the lowercase user input
        return "Hello there! It's lovely to chat with you." # Return a greeting message
    elif any(farewell in user_input_lower for farewell in farewells): # Check if any farewell word is present
        return "Goodbye for now! Feel free to reach out again anytime." # Return a farewell message
    elif any(thank in user_input_lower for thank in thanks): # Check if any thank word is present
        return "You're most welcome! Glad I could help." # Return a message acknowledging thanks
    elif any(weather in user_input_lower for weather in weather_queries): # Check if any weather-related phrase is present
        return "Ah, the weather! While I don't have live updates, I hope it's pleasant where you are." # Return a message about the weather
    elif any(joke in user_input_lower for joke in joke_queries): # Check if any joke-related phrase is present
        jokes = [ # Define a list of jokes
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common... it's a shame they'll never meet.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        return random.choice(jokes) # Return a randomly selected joke
    elif any(fact in user_input_lower for fact in fact_queries): # Check if any fact-related phrase is present
        facts = [ # Define a list of interesting facts
            "Did you know that honey never spoils?",
            "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
            "A group of flamingos is called a 'flamboyance'."
        ]
        return random.choice(facts) # Return a randomly selected fact
    elif any(hobby in user_input_lower for hobby in hobby_queries): # Check if any hobby-related phrase is present
        return "As a digital entity, I don't have hobbies in the human sense. However, I thoroughly enjoy processing information and assisting users like you!" # Return a message about the chatbot's "hobbies"
    elif any(help_query in user_input_lower for help_query in help_queries): # Check if any help-related phrase is present
        return "I can respond to greetings, offer simple facts or jokes, and acknowledge your thanks. Just try typing something!" # Return a message explaining the chatbot's capabilities
    elif any(name in user_input_lower for name in name_queries): # Check if any name-related phrase is present
        return "I am The Curious Buddy, here to assist and engage!" # Return the chatbot's name
    elif any(feeling in user_input_lower for feeling in feeling_queries): # Check if any feeling-related phrase is present
        return "As a chatbot, I don't experience feelings, but I'm functioning optimally and ready to help!" # Return a message about the chatbot's lack of feelings
    else: # If none of the predefined patterns match
        return "That's an interesting thought! While I don't have a specific answer for that right now, feel free to ask something else." # Return a default response for unknown inputs

# Let's test it out!
while True: # Start an infinite loop for continuous conversation
    user_input = input("You: ") # Get input from the user
    if user_input.lower() == "exit": # Check if the user typed "exit" to end the conversation
        print("The Curious Buddy: It was a pleasure chatting with you!") # Print a farewell message from the chatbot
        break # Exit the loop, ending the conversation
    response = curious_buddy(user_input) # Call the 'curious_companion' function to get a response based on the user input
    print("The Curious Buddy:", response) # Print the chatbot's response