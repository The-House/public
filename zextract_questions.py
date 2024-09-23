import yaml

# Path to the WikiQA train dataset
file_path = '/Users/colton.chladek/Library/CloudStorage/OneDrive-KE/Desktop/Dev/Dev-Box/CSC525/PortfolioProject/WikiQACorpus/WikiQA-train.txt'

# Load the data from the WikiQA file
def extract_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        for line in file:
            # Splitting each line into question, answer, and relevance
            parts = line.strip().split('\t')
            if len(parts) == 3 and parts[2] == '1':  # Only consider relevant questions
                question = parts[0].strip()
                questions.append(question)
    return questions

# Get the extracted questions
questions = extract_questions(file_path)

# Create Rasa NLU format
nlu_data = {
    'version': '3.1',
    'nlu': [
        {
            'intent': 'ask_question',
            'examples': '\n'.join([f'- {q}' for q in questions if len(q) < 200])  # Properly formatted YAML block
        }
    ]
}

# Path to store the new nlu.yml file
output_path = '/Users/colton.chladek/Library/CloudStorage/OneDrive-KE/Desktop/Dev/Dev-Box/CSC525/PortfolioProject/data/nlu.yml'

# Save to nlu.yml in YAML format
with open(output_path, 'w') as file:
    yaml.dump(nlu_data, file, default_flow_style=False, sort_keys=False)

print(f"NLU data saved to {output_path}")
