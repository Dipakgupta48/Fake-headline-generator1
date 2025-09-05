# 1- import the random module
import random

# 2- create subjects list
subjects = ["The cat",
            "A dog",
            "The president",
            "A scientist", 
            "The teacher",
            "An artist",
            "The athlete",
            "A musician",  
            "The chef",
            "A programmer",
            "The doctor",
            "A writer",
            "The engineer",
            "A dancer",
            "The firefighter",
            "A pilot",
            "A farmer",
            "A detective",
            "The librarian",
            "A gardener",
            "The mechanic",
            "A photographer",
            "The architect",
            "A nurse",]

actions= ["jumps over",
          "runs to",
          "writes about",
          "discovers",
          "paints",
          "teaches",
          "sings to",
          "dances with",
          "cooks for",
          "codes",
          "heals",
          "designs",
          "drives",
          "plants",
          "investigates",
          "reads to",
          "fixes",
          "captures",
            "builds",
            "nurses",
            "explores",
            "creates",
            "analyzes",
            "innovates",
                "transforms",]


places_or_things=["the fence",
                  "the park",
                    "the book",
                    "a new element",
                    "a masterpiece",
                    "the classroom",
                    "a song",   
                    "the stage",
                    "a gourmet meal",
                        "a new app",
                        "a patient",
                        "a skyscraper",
                        "the airplane",
                        "the field",
                        "a mystery",
                        "the library",
                        "the car",
                        "the perfect shot",
                        "a sustainable garden",]

# 3-start the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input != 'yes':
        print("Thank you for using the fake headline generator. Goodbye!")
        break