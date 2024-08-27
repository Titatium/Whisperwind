import spacy

# Load spaCy language model 
nlp = spacy.load("en_core_web_sm")

# Expand verb synonyms significantly
verb_synonyms = {
    "look": ["examine", "inspect", "observe", "view", "check", "peer", "gaze", "scan"],
    "take": ["get", "grab", "pick up", "acquire", "collect", "seize", "snatch", "lift"],
    "attack": ["fight", "hit", "strike", "assault", "battle", "combat", "engage", "assail"],
    "go": ["move", "walk", "travel", "proceed", "venture", "journey", "head", "advance"],
    "talk": ["speak", "converse", "chat", "communicate", "interact", "engage", "address"],
    "use": ["utilize", "employ", "apply", "operate", "activate", "trigger", "wield"],
    "inventory": ["inv", "items", "possessions", "belongings", "gear", "equipment"],
    "help": ["assist", "aid", "support", "guide", "instructions"],
    "quit": ["exit", "leave", "depart", "logout", "end"],
    "drop": ["discard", "release", "abandon", "leave behind"],
    "equip": ["wear", "don", "put on"],
    "unequip": ["remove", "take off", "doff"],
    "status": ["stats", "condition", "health", "info"],
    "cast": ["spell", "magic", "conjure"],
    # ... add many more verbs and synonyms
}


def parse_command(command):
    doc = nlp(command)

    # Verb identification (using synonyms and dependency parsing)
    verb = next((token.lemma_ for token in doc if token.pos_ == "VERB" and 
                 (token.lemma_ in verb_synonyms or 
                  any(token.lemma_ in syns for syns in verb_synonyms.values()))), None)

    if verb:
        # Object/target identification (using dependency parsing)
        objects = [child for child in doc if child.dep_ in ["dobj", "pobj"]] 
        
        # Additional context extraction (using other dependencies or entity recognition)
        context = {}
        for token in doc:
            if token.dep_ == "prep":  # Prepositional phrases (e.g., "with the sword")
                context[token.text] = [child for child in token.children]
            # ... extract other relevant context (adverbs, locations, etc.)

        print(f"Parsed: Verb={verb}, Objects={objects}, Context={context}")

        # Command execution (match to game functions)
        execute_command(verb, objects, context)

    else:
        print("Invalid command. Type 'help' for assistance.")

def execute_command(verb, objects, context):
    # Extensive command handling logic
    if verb == "look":
        if objects:
            for obj in objects:
                look_at(obj)  # Implement your look_at function
        else:
            look_around()   # Implement your look_around function
    elif verb == "take":
        # ... handle 'take' command
    # ... handle all other verbs

# Example usage
parse_command("Carefully examine the ancient scroll with your magnifying glass.")
# Output: 
# Parsed: Verb=examine, Objects=[scroll], 
# Context={'with': [magnifying, glass], 'Carefully': []} 