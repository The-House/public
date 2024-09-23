import random

# Base examples for each intent (including all of your provided examples)
base_examples = {
    "ask_hazard": [
        "What is an arc flash hazard?",
        "How dangerous is electrical work?",
        "What are the risks of an arc flash?",
        "Can electrical work cause injury?",
        "What hazards are associated with high-voltage work?",
        "What types of hazards exist in electrical work?",
        "How can an arc flash occur?",
        "What are the common electrical hazards on a job site?",
        "What are the main dangers of working near power lines?",
        "What injuries can occur from arc flash?",
        "Is arc flash a common hazard in electrical work?",
        "How does an arc flash happen?",
        "Can you explain what an arc flash is?",
        "What causes electrical hazards?",
        "Are electrical hazards dangerous for untrained workers?",
        "What can cause an arc flash explosion?",
        "What is the danger of working with high-voltage electricity?",
        "How can electrical shock occur?",
        "What are the dangers of electrical burns?",
        "Can electrical work lead to fires?",
        "Are there fire hazards related to arc flash?",
        "What is an arc blast?",
        "What injuries can an arc blast cause?",
        "Can electrical hazards be fatal?",
        "What are the most common causes of electrical hazards?",
        "How do arc flashes affect electrical equipment?",
        "What kind of PPE protects against arc flash hazards?",
        "What are the most common arc flash injuries?",
        "How do you prevent arc flash hazards?",
        "Can electrical hazards affect the environment?",
        "How do workers avoid electrical hazards?",
        "How can electrical equipment be hazardous?",
        "Are wet conditions dangerous when working with electricity?",
        "How can arc flash injuries be treated?",
        "What voltage is most associated with arc flash hazards?",
        "How do arc flashes differ from electrical shocks?",
        "What happens if you don't follow safety procedures in electrical work?",
        "How dangerous is live electrical work?",
        "What are the potential long-term effects of electrical injuries?",
        "What training is required to understand electrical hazards?",
        "Can poorly maintained equipment cause electrical hazards?",
        "How does grounding help prevent electrical hazards?",
        "What is the likelihood of an arc flash in residential electrical work?",
        "How dangerous is electrical wiring in old buildings?",
        "What makes high-voltage systems more dangerous than low-voltage?",
        "What are the symptoms of arc flash exposure?",
        "What types of electrical systems are most prone to hazards?",
        "How can workers detect electrical hazards in the field?",
        "How do electrical currents contribute to workplace hazards?"
    ],
    "ask_ppe": [
        "What PPE is needed for working with 600V?",
        "Do I need gloves for electrical work?",
        "What type of PPE should I wear for high-voltage work?",
        "Should I wear eye protection when working with electricity?",
        "How do I choose the right PPE for electrical work?",
        "What kind of helmet is required for electrical workers?",
        "Do I need insulated tools when working with electricity?",
        "What kind of gloves should be used for electrical tasks?",
        "Is face protection required for electrical work?",
        "Can regular gloves be used for electrical work?",
        "What type of clothing is considered PPE for electrical work?",
        "Do I need arc-rated PPE for all electrical tasks?",
        "What is arc-rated PPE?",
        "How does arc-rated PPE protect workers?",
        "What is the best PPE for arc flash protection?",
        "How much PPE is required for electrical maintenance?",
        "Are there different PPE requirements for low-voltage work?",
        "Can PPE protect me from electrical shocks?",
        "What PPE is recommended for working near high-voltage lines?",
        "What PPE is needed for live electrical work?",
        "How do I know if my PPE is rated for electrical work?",
        "Is PPE mandatory when working with electricity?",
        "Can PPE prevent all electrical injuries?",
        "What PPE should be worn in an electrical substation?",
        "How do you maintain PPE for electrical work?",
        "Can I use regular safety boots for electrical work?",
        "Do electricians need to wear flame-resistant clothing?",
        "What PPE is required for working with energized circuits?",
        "Can I reuse my PPE after an arc flash incident?",
        "What PPE standards should be followed for electrical work?",
        "Should I wear a full-body suit for high-voltage electrical tasks?",
        "Do I need ear protection for electrical work?",
        "Is head protection required for all electrical tasks?",
        "What type of boots should I wear for electrical tasks?",
        "How often should I inspect my electrical PPE?",
        "What PPE do I need for electrical panel work?",
        "Is there specific PPE for arc flash hazards?",
        "How do I know if my PPE is safe for electrical tasks?",
        "Can PPE reduce the risk of electrical burns?",
        "Do electricians need respiratory protection?",
        "What PPE is recommended for circuit breaker maintenance?",
        "Are safety glasses enough for electrical work?",
        "What does PPE stand for in electrical safety?",
        "How effective is PPE in preventing electrical injuries?",
        "Can I use cotton clothing for electrical tasks?",
        "What protective clothing is recommended for electrical engineers?",
        "What type of PPE should be worn for high-voltage cable work?",
        "Should I wear PPE when working near transformers?",
        "What are the most common PPE items for electricians?",
        "How does PPE help prevent arc flash injuries?"
    ],
    "ask_voltage": [
        "What is the safe voltage limit for working?",
        "How much voltage is dangerous without protection?",
        "What voltage requires special PPE?",
        "What is the maximum safe voltage for electricians?",
        "What voltage is considered high-voltage?",
        "Is there a safe voltage for electrical work?",
        "Can I work on 120V circuits without protection?",
        "How much voltage is dangerous in water?",
        "Is 600V more dangerous than 480V?",
        "What voltage is considered low-voltage in electrical work?",
        "Is low-voltage safer than high-voltage?",
        "What voltage level is common in residential wiring?",
        "How does voltage affect the risk of electric shock?",
        "What voltage requires insulated tools?",
        "How much voltage can the human body handle safely?",
        "At what voltage does arc flash become a risk?",
        "What is the difference between high and low-voltage safety?",
        "Do I need PPE for 120V electrical work?",
        "Can voltage affect the severity of electrical burns?",
        "What voltage requires a full PPE kit?",
        "How does voltage affect electrical equipment ratings?",
        "Is 240V safe to work on without gloves?",
        "At what voltage do you need to de-energize equipment?",
        "What is the minimum voltage considered hazardous?",
        "What voltage poses the highest risk for arc flash?",
        "What voltage level requires an arc flash suit?",
        "How does voltage contribute to electrical fires?",
        "What voltage is used in commercial electrical systems?",
        "What voltage is found in industrial settings?",
        "Is it safe to work on 480V systems with minimal PPE?",
        "What is the voltage limit for residential electricians?",
        "How can I measure the voltage in a live circuit?",
        "What voltage rating is needed for electrical gloves?",
        "Is it safe to touch 12V wires without PPE?",
        "What is the voltage rating of a typical circuit breaker?",
        "How can you reduce the voltage hazard in electrical work?",
        "What voltage should electricians be trained to handle?",
        "How dangerous is 1000V compared to lower voltages?",
        "What voltage is typical in high-voltage electrical systems?",
        "Does voltage affect the need for grounding?",
        "How does voltage influence the choice of PPE?",
        "What is the voltage rating for arc flash protection?",
        "How much voltage is in standard household outlets?",
        "What voltage requires a safety permit for work?",
        "How can I check if a circuit is live and its voltage level?",
        "Is 600V considered high-voltage in electrical terms?",
        "How does voltage increase the risk of electrocution?",
        "What voltage is used for high-tension power lines?",
        "Is there a limit to how much voltage can be worked on safely?"
    ]
}

# Synonyms for key terms
synonyms = {
    "arc flash": ["electrical arc", "voltage flash", "electric spark", "high-voltage arc"],
    "hazard": ["danger", "risk", "peril", "threat"],
    "dangerous": ["risky", "hazardous", "unsafe", "perilous"],
    "work": ["task", "job", "activity", "operation"],
    "injury": ["harm", "damage", "wound", "trauma"],
    "high-voltage": ["high power", "high amperage", "high wattage", "high current"],
    "PPE": ["personal protective equipment", "safety gear", "protective gear", "safety equipment"],
    "voltage": ["electrical power", "current", "amperage", "electrical voltage"],
    "insulated": ["shock-resistant", "electrically safe", "protected", "shielded"],
    "equipment": ["tools", "devices", "gear", "apparatus"],
    "gloves": ["hand protection", "insulating gloves", "safety gloves", "shock-resistant gloves"]
}

# Function to augment sentences by replacing words with synonyms
def augment_sentence(sentence, synonyms):
    words = sentence.split()
    augmented_sentence = " ".join([random.choice(synonyms.get(word, [word])) for word in words])
    return augmented_sentence

# Generate augmented examples
def generate_augmented_examples(base_examples, synonyms, n=5):
    augmented_examples = {}
    for intent, examples in base_examples.items():
        augmented_examples[intent] = []
        for example in examples:
            # Generate 'n' variations for each base example
            for _ in range(n):
                augmented_sentence = augment_sentence(example, synonyms)
                augmented_examples[intent].append(augmented_sentence)
    return augmented_examples

# Generate 5 augmented examples for each base sentence
augmented_data = generate_augmented_examples(base_examples, synonyms, n=5)

# Display the generated examples
for intent, examples in augmented_data.items():
    print(f"Intent: {intent}")
    for example in examples:
        print(f" - {example}")
    print("\n")