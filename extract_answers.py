import yaml

# Path to the WikiQA train dataset
file_path = '/Users/colton.chladek/Library/CloudStorage/OneDrive-KE/Desktop/Dev/Dev-Box/CSC525/PortfolioProject/WikiQACorpus/WikiQA-train.txt'  # Update this to the correct file path

# Load the data from the WikiQA file and extract answers
def extract_answers(file_path):
    answers = []
    with open(file_path, 'r') as file:
        for line in file:
            # Splitting each line into question, answer, and relevance
            parts = line.strip().split('\t')
            if len(parts) == 3 and parts[2] == '1':  # Only consider relevant answers (label 1)
                answer = parts[1].strip()  # The second column is the answer
                answers.append(answer)
    return answers

# Get the extracted answers
answers = extract_answers(file_path)

# Format the answers for Rasa's domain.yml (under 'utter_ask_question')
def format_answers_for_domain(answers):
    responses = []
    for answer in answers:
        response_entry = f"    - text: \"{answer}\""
        responses.append(response_entry)
    return responses

# Write the formatted answers to a text file for easy integration
output_file = 'utter_ask_question_responses.txt'

with open(output_file, 'w') as file:
    file.write("utter_ask_question:\n")
    formatted_answers = format_answers_for_domain(answers)
    file.write("\n".join(formatted_answers))

print(f"Formatted answers saved to {output_file}")
