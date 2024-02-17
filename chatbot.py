import spacy
from spacy.matcher import Matcher
import random

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

patterns_responses = {
    "greeting": (["hello", "hi", "hey"], [
        "Hi there! What's on your mind today?",
        "Hey! How can I assist you?",
        "Hello! Feel free to ask me anything."
    ]),
    "question": (["what", "how", "why"], [
        "Sure, I'll try my best to answer that.",
        "Let me see what I know about that...",
        "Ask away! I'm always learning."
    ]),
    "about_me": (["tell", "about", "yourself"], [
        "I'm a chatbot under development, learning to have conversations like you and me!",
        "I don't have a physical body, but I can access and process information from the real world.",
        "I'm still learning, but I'm excited to see what I can do in the future!"
    ]),
    "like": (["like"], [
        "Hmm, that's an interesting question. I don't really have preferences like humans do, but I enjoy processing information and learning new things.",
        "As a language model, I don't have personal opinions or feelings, but I can tell you what people generally like about different things.",
        "Tell me more about what you like! I'm always curious to learn about different perspectives."
    ]),
    "how_feeling": (["how"], [
        "I don't have emotions like humans do, but I can analyze patterns in language to understand sentiment. How are you feeling today?",
        "It's always great to hear how people are doing. Tell me more about your day!",
        "I'm happy to hear you're doing well! Is there anything I can do to help?"
    ]),
    "joke": (["joke"], [
        "What do you call a fish with no eyes? Fsh!",
        "What do you call a lazy kangaroo? Pouch potato!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ])
    
}

for intent, (keywords, _) in patterns_responses.items():
    patterns = [[{"LOWER": keyword}] for keyword in keywords]  # Wrap each pattern in a list
    matcher.add(intent, patterns)

def respond(input_text):
    doc = nlp(input_text)
    matches = matcher(doc)
    if matches:
        intent = nlp.vocab.strings[matches[0][0]]
        _, responses = patterns_responses[intent]
        return random.choice(responses)
    else:
        return "Sorry, I don't understand. Can you try rephrasing?"


while True:
    user_input = input("You: ")  
    response = respond(user_input)  
    print("Chatbot:", response)
