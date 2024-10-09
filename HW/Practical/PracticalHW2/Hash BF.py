import string
import itertools
import hashlib

# set the length of the secret
n = int(input("Enter the length of the secret: "))


# read alphabet file
with open('alpha.txt', 'r') as f:
    alphabet = f.read().strip()

# generate all possible combinations
combinations = []

for c in itertools.product(alphabet, repeat=n):
    combinations.append(''.join(c))

with open("main.txt", "rb") as main:
    main_hash = hashlib.sha256(main.read()).hexdigest()

guess_num = 0
# loop to generate guess secrets and check their hash value
for i in range(len(combinations)):
    # generate guess secret
    guess_secret = combinations[i]
    
    # write guess secret to file
    with open('guess.txt', 'w') as f:
        f.write(guess_secret)
        f.close()
    # get hash of guess secret
    with open('guess.txt', 'rb') as f:
        guess_hash = hashlib.sha256(f.read()).hexdigest()
        f.close()

    # increment guess counter
    guess_num += 1
    
    # check if guess hash matches main hash
    if guess_hash == main_hash:
        print(f"Match found after {guess_num} guesses! : {guess_secret}")
        break
    else:
        print(f"Guess #{guess_num}: {guess_secret} ({guess_hash})")
