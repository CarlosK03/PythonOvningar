characters = []
uses = []
text=str(input("Please input text: "))

def find_length(text): #Homebaked len() :)
    count = 0
    for c in text:
        count += 1
    return count

def lower(text): #Homecooked lower()
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for c in text:
        if c not in lowers + uppers:
            # Adding the character to the output string.
            output += c
            continue
       # Checking if the character is in the alphabet.
        for index in range(26):
            upper_char = uppers[index]
            lower_char = lowers[index]
            if c == upper_char or c == lower_char:
                output += lower_char
                break
    return output

for c in text:
    if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        c = lower(c)
        for i in range(find_length(characters)):
            item = characters[i]
            if c == item:
                uses[i] += 1
                break
        else: # Character has not been added to the list of character counts yet.
            characters.append(c)
            uses.append(1)

most_use = 0 # Set lower bound
most_character = None
least_use = find_length(text) # Set upper bound
least_character = None
for character, use in zip(characters, uses):
    if use < least_use:
        least_use = use
        least_character = character
    if use > most_use:
        most_use = use
        most_character = character

print("The most used character is:", most_character, "with a usage of", most_use, "times.")
print("The least used character is:", least_character, "with a usage of", least_use, "times.")