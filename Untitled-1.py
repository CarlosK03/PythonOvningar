text = input("Enter Text: ")
# remove spaces. comma, dot and make everything lowercase
text = text.replace(" ", "").replace(",", "").replace(".", "").lower()


# a function for counting the letters in a text, function returns an int,
# for every time it finds the current letter in the text you add 1 to the count:
def frequency_of_letter(current_letter) -> int:
    number = 0
    for letter in text:
        if current_letter == letter:
            number += 1
    return number


highestFrequency = 0    # before it starts counting, the highest frequency is set to 0
# because it will always be higher than 0.
mostFrequentLetter = ""     # we don't know our most frequent letter yet. for now, it is empty.
# The first time this programme runs the first letter will become the most and least frequent letter.
lowestFrequency = len(text)     # lowest frequency is set to the length of the text. Could also be set to a really high number if len() is not allowed.
# It will always end up lower (or same) as the entire text.
leastFrequentLetter = ""    # same thing here as for most frequent letter.

# a loop that looks at each character in the text and compares the frequencies.
for letter in text:
    currentFrequency = frequency_of_letter(letter)  # function calculates letter frequency
    if currentFrequency >= highestFrequency and letter not in mostFrequentLetter:   # if the letter occurs more often (or equal) AND hasnt been added yet, then:
        if currentFrequency == highestFrequency:    # in case there are multiple letters with same highest frequency:
            mostFrequentLetter += letter            # add letter to most frequent letter.
        else:
            highestFrequency = currentFrequency     # otherwise the current frequency becomes the highest frequency
            mostFrequentLetter = letter             # and the letter becomes the most frequent letter.
    if currentFrequency <= lowestFrequency and letter not in leastFrequentLetter:   # if the letter occurs less often (or equal) AND hasnt been added yet, then:
        if currentFrequency == lowestFrequency:     # if equal count :
            leastFrequentLetter += letter           # add the new letter.
        else:                                       # if letter occurs less often, then:
            lowestFrequency = currentFrequency      # update the lowest frequency
            leastFrequentLetter = letter            # and update the least frequent letter

print(f"Most frequent letter(s): {mostFrequentLetter} with frequency {highestFrequency},\nleast frequent letter(s): {leastFrequentLetter} with frequency {lowestFrequency}")

input()