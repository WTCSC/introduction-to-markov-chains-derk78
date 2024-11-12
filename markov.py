import random
import argparse

text = "The practical thing was to find rooms in the city but it was a warm season and I had just left a country of wide lawns and friendly trees so when a young man at the office suggested that we take a house together in a commuting town it sounded like a great idea He found the house a weather beaten cardboard bungalow at eighty a month but at the last minute the firm ordered him to Washington and I went out to the country alone I had a dog at least I had him for a few days until he ran away and an old Dodge and a Finnish woman who made my bed and cooked breakfast and muttered Finnish wisdom to herself over the electric stove"
transitions = {}

#split the text into a words in a list
words = text.split()

for i in range(len(words) - 1):
    #Make the current word lowercase since we'll add in capitalization later on.
    current_word = words[i].lower()
    #Take the current word represented by i and add 1 for the next word after the current one
    next_word = words[i + 1]
    
    #If the current word isn't in the transitions already add it.
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)
    
def generate_text(start_word, num_words):
    #Create a flag system to capitalize the next word after a period shows up. Set it to true at the start since the first letter of the text should be capitalized
    period = True
    current_word = start_word.lower()
    
    #Result array will begin empty since we'll add words to it as we go through the loop.
    result = []
    sentence_length = 0 
    
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            sentence_length += sentence_length
        else:
            break

        if period:
            current_word = current_word.capitalize()
            period = False

        sentence_length += 1
        
        if sentence_length >= 5 and random.random() < 0.2:
            period = True
            result[-1] += "."
            sentence_length = 0
        elif random.random() < 0.1:
            result[-1] += ","

        #current_word = next_word
        result.append(current_word)
        current_word = next_word

    output = " ".join(result)
    return output


user_input = input()
print(generate_text(user_input, 100))

def main():
    parser = argparse.ArgumentParser(description='Generate random text')
    parser.add_argument('Start_word', type=str, help='The first word needed for text generation.')
    parser.add_argument("num_words", type=int, help="The number of words you want to generate.")
    parser.add_argument("text", type=str, help="The text needed to build the string.")
    args = parser.parse_args()
