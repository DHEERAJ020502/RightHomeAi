import json
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('RightHomeAI')

# Train the chatbot with some basic responses
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Load property dataset from JSON file
property_dataset_path = os.path.join('property_dataset', 'properties.json')
with open(property_dataset_path, 'r') as file:
    properties = json.load(file)

def get_property_recommendations(user_preferences):
    # Simple scoring based on user preferences
    recommendations = []
    for property in properties:
        score = property['score']  # This should be calculated based on user preferences
        if score >= user_preferences['min_score']:
            recommendations.append(property)
    return recommendations

def chat():
    print("Hello! I'm RightHomeAI. How can I assist you with property recommendations?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("RightHomeAI: Goodbye!")
            break
        elif "recommend" in user_input:
            user_preferences = {'min_score': 80}  # Example user preference
            recommendations = get_property_recommendations(user_preferences)
            if recommendations:
                for prop in recommendations:
                    print(f"RightHomeAI: I recommend a property in {prop['location']} priced at ${prop['price']} with size {prop['size']} sqft.")
            else:
                print("RightHomeAI: Sorry, no properties match your criteria.")
        else:
            response = chatbot.get_response(user_input)
            print(f"RightHomeAI: {response}")

if __name__ == "__main__":
    chat()