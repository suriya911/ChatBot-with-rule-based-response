import random
import spacy
from fuzzywuzzy import fuzz

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define a dictionary of predefined rules and responses
rules_responses = {
    "hi": ["Hello!", "Hey there!", "Hi! How's it going?"],
    "how are you": ["I'm doing well, thanks for asking!", "Pretty good, how about you?"],
    "what's your name": ["I'm your friendly chatbot friend!", "I'm just a chatbot here to chat with you!"],
    "bye": ["Goodbye!", "Bye! Come back soon!", "See you later!"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                       "What do you call an alligator in a vest? An investigator!", 
                       "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "how's the weather": ["I'm not sure, but you can check your local weather forecast!", 
                          "I'm indoors, so I'm not affected by the weather!"],
    "what are you up to": ["Just here, chatting with you!", "Nothing much, just being a chatbot!"],
    "do you like music": ["I don't have ears, but I can appreciate music!", "Music is nice, even for chatbots!"],
    "do you have any pets": ["I'm just a digital entity, so I don't have pets!", "Nope, no pets for me!"],
    "what's your favorite food": ["I don't eat, but I hear good things about binary code!", "I'm a chatbot, so I don't have taste buds!"],
    "have you seen any good movies lately": ["I don't watch movies, but I've heard good things about some classics!", "Nope, no movies for me!"],
    "how's your day been": ["It's been good, especially now that I'm chatting with you!", "Pretty uneventful, but chatting with you makes it better!"],
    "what's new with you": ["Not much, just hanging out in the digital realm!", "Same old, same old!"],
    "how's work/school": ["I don't have a job or attend school, but I'm here to chat with you!", "Work/school is non-existent in my world!"],
    "what are your hobbies": ["I don't have hobbies, but I'm always here to chat!", "Chatting with you is my favorite pastime!"],
    "are you a morning person or a night owl": ["I'm a 24/7 chatbot, so I'm always here whenever you need me!", "I'm always awake and ready to chat, whether it's morning or night!"],
    "do you believe in aliens": ["I'm not sure, but the universe is vast, so who knows!", "It's an interesting concept to think about!"],
    "what's your favorite color": ["I don't have eyes, but I've heard good things about blue!", "I'm a chatbot, so I don't have preferences for colors!"],
    "are you a cat person or a dog person": ["I don't have preferences for pets, but both cats and dogs are adorable!", "I'm a chatbot, so I don't have opinions on pets!"],
    "what's your dream vacation destination": ["I don't have dreams, but a virtual vacation sounds nice!", "Anywhere with a stable internet connection would be ideal for me!"],
    # Add more rules and responses as needed based on user input patterns and context of conversation 
}

# Function to preprocess user input using spaCy
def preprocess_input(user_input):
    doc = nlp(user_input.lower())
    processed_input = " ".join([token.lemma_ for token in doc])
    return processed_input

# Function to generate response based on preprocessed user input
def generate_response(user_input):
    # Check if preprocessed input is empty
    if not user_input:
        return "Hmm, I didn't catch that. Could you please rephrase?"
    # Check for greetings
    if any(word in user_input.lower() for word in ['hi', 'hello', 'hey']):
        return random.choice(rules_responses['hi'])
    # Check for simple sentiments
    elif any(word in user_input.lower() for word in ['good', 'great', 'fine', 'well']):
        return "That's nice to hear!"
    elif any(word in user_input.lower() for word in ['bad', 'not good', 'terrible']):
        return "I'm sorry to hear that. Is there anything I can do to help?"
    else:
        # Calculate similarity score between user input and each rule
        scores = [(rule, fuzz.partial_ratio(user_input, rule)) for rule in rules_responses.keys()]
        # Sort scores in descending order of similarity
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Check if highest similarity score is above a certain threshold
        if scores[0][1] >= 70:
            return random.choice(rules_responses[scores[0][0]])
        else:
            # If no rule matches and no response to previous message detected, generate a generic response
            return "Hmm, I'm not sure what you mean. Can you try rephrasing your question?"

# Main function to handle user interaction
def main():
    print("Welcome! I'm your chatbot friend. Feel free to chat with me!")
    print("You can say 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot Friend: Goodbye! It was nice chatting with you!")
            exit()
        else:
            preprocessed_input = preprocess_input(user_input)
            response = generate_response(preprocessed_input)
            print("Chatbot Friend:", response)

if __name__ == "__main__":
    main()
