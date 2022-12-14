
secret = "car"
n_trials = 10

current_trial = 0
guessed = False
my_secret=""

while not guessed and (current_trial<n_trials):
    letter=input("write a letter: ")
    if letter:
        letter=letter[0]

    if letter in secret:
        my_secret += letter
    
    current_trial+=1
    
    if secret==my_secret:
        guessed=True
        
        