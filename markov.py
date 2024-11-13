import random
import argparse

text = "The practical thing was to find rooms in the city but it was a warm season and I had just left a country of wide lawns and friendly trees so when a young man at the office suggested that we take a house together in a commuting town it sounded like a great idea He found the house a weather beaten cardboard bungalow at eighty a month but at the last minute the firm ordered him to Washington and I went out to the country alone I had a dog at least I had him for a few days until he ran away and an old Dodge and a Finnish woman who made my bed and cooked breakfast and muttered Finnish wisdom to herself over the electric stove"
transitions = {}

#split the text into words in an array.
words = text.split()

#Using the reference text build a transitions dictionary for the markov chain.
#For every word in the reference text add the next word to the `transitions` dictionary as a possible next word.
for i in range(len(words) - 1):
    current_word = words[i].lower()
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)
    
def generate_text(start_word, num_words):
    #Create a flag system to capitalize the next word after a period shows up. 
    #Capitalize the first word by setting it to true and then add in random commas and periods afterwards in the for loop.
    period = True
    current_word = start_word.lower()
    result = []
    sentence_length = 0 
    
    #If the current word is in the transitions dictionary then randomly choose a new word if not break the loop. We will also add 1 to the sentence length for each new word.
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            sentence_length += 1
        else:
            break

        #Once a period is added and flagged we'll capitalize the word after the period and reset our `period` variable to false.
        if period:
            current_word = current_word.capitalize()
            period = False

        sentence_length += 1
        
        #Here is where we set up the conditions for a period or a comma to be added. 
        #There is a 20 percent chance of a period being added when the sentence is 5 or more characters, and a ten percent chance of a comma being added. 
        #We will also reset our sentence length to 0 to reset the count.
        if sentence_length >= 5 and random.random() < 0.2:
            period = True
            result[-1] += "."
            sentence_length = 0
        elif random.random() < 0.1:
            result[-1] += ","

        #Here we append the words that build our text to the result variable.
        result.append(current_word)
        current_word = next_word

    #Finally we join our result array with spaces to complete the output text, and return it.
    output = " ".join(result)
    return output

#Here we have our function `generate_text` accept user input and the length wanted.
user_input = input()
print(generate_text(user_input, 100))

#Create our script using our function and define the arguments were passing in.
def main():
    parser = argparse.ArgumentParser(description='Generate random text')
    parser.add_argument('start_word', type=str, help='The first word needed for text generation.')
    parser.add_argument("num_words", type=int, help="The number of words you want to generate.")
    args = parser.parse_args()

    generated_text = generate_text(args.start_word, args.num_words)
    print(generated_text)

if __name__ == "__main__":
    main()