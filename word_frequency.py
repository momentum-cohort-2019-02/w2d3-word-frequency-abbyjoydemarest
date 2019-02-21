import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def only_lower_case_letters(text):
    """Take the text from the file, lower case all letters, and get rid of everything except letters. """
    #lower case the letters by calling the .casefold function
    text = text.casefold()
    #get all valid characters by calling the function on the string to find all letters, whitespaces and digits
    valid_characters = string.ascii_letters + string.whitespace + string.digits
    #remove all punctuation but createing a new list
    new_text = ""
    #run a for loop to run through each character one at a time from the original text and make a new string
    for character in text:
        #aif the character in the text is in valid_character then add it to the new_text
        if character in valid_characters:
            #add it to new_text
            new_text += character
    #make text be equal to new_text string
    text = new_text
    #replace "/n" with a space
    text = text.replace("\n", " ")
    #get the string :)
    print(text)
    return text

def print_word_freq(filename):
    """Read in `file_name` and print out the frequency of words in that file."""
    #get the file
    with open(filename) as file:
        #close it once the file has been read
        text = file.read()

    #clean up the text witht he function above
    text = only_lower_case_letters(text)
    #create a new list, which will convert the string to a list
    words = []
    #remove extra white space and do a for loop that says for each word if it is not a space or a stop word then add it to the wrds list
    for word in text.split(" "):
        #if the word is a space or a STOP WORD then do not add it to the list, but if it is that dont add it to the list
        if word != '' and word not in STOP_WORDS:
            #the add to word
          words.append(word)
          print(words)

    return words


def character_frequency(words):
    #create a list of the frequency of each word in the filename
    character_count = {}
    #call the list of word from above and find the frequency of each word in that list, If ther word is in words then
    for character in words:
        #if the character in the dictionary frequency is found in the frequency then count it as a time that that character is in the frequency 
        if character in character_count:
            #if a character is not in the frequency then count it once.
            character_count[character] = character_count[character] + 1
        else:
            
            #if a character is now in frequency then count it again.
            character_count[character] = 1
    print(character_count)
    return character_count

print(" ".join(print_word_freq(only_lower_case_letters)))
character_count = character_frequency(string)
print(character_count)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print(print_word_freq(file))
    else:
        print(f"{file} does not exist!")
        exit(1)
