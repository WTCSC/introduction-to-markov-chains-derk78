import random

"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""
text = "The practical thing was to find rooms in the city but it was a warm season and I had just left a country of wide lawns and friendly trees, so when a young man at the office suggested that we take a house together in a commuting town it sounded like a great idea. He found the house, a weather beaten cardboard bungalow at eighty a month, but at the last minute the firm ordered him to Washington and I went out to the country alone. I had a dog, at least I had him for a few days until he ran away, and an old Dodge and a Finnish woman who made my bed and cooked breakfast and muttered Finnish wisdom to herself over the electric stove."
transitions = {}
punctuation = {".","?","!",}

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""
words = text.split()
for i in range(len(words) - 1):
    current_word = words[i]
    #for char in current_word:
        #make sure that if punctuation if found end the sentence from which word the punctuation was found 
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)
    

"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:

1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string

TODO: Clean up the generated text for better formatting and readability,
e.g., capitalization, punctuation, line breaks, etc.
"""
def generate_text(start_word, num_words):
    current_word = start_word
    result = [current_word.capitalize()]
    sentence_length = 0 
    
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            if sentence_length >= 5 and random.random() < 0.2:
                result[-1] += "."
                current_word = current_word.capitalize()
                sentence_length = 1
            elif random.random() < 0.1:
                result[-1] += ","
                
            result.append(next_word)
            current_word = next_word
            sentence_length += 1 
        else:
            break
        
    text_output = " ".join(result)
    text_output = text_output.replace(". ", ".\n")  
    return text_output


user_input = input()
print(generate_text(user_input, 100))
    # for _ in range(num_words - 1):
    #     if current_word in transitions:
    #         next_word = random.choice(transitions[current_word])
    #         result.append(next_word)
    #         current_word = next_word
    #     else:
    #         break
    # return " ".join(result)

"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""
# user_input = input()
# print(generate_text(user_input, 100))



#make it so that It will accept however many characters I want it to generate.