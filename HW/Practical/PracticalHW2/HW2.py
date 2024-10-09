"""
in the name of god
advanced cryptography practical hw2
Pouria Dadkhah - 401201381

in this code we updated Hash BF code in these parts:
    use filehash library to hash a file instead of its content
    instead of creating whole combination list and then check their hash values, checking the hash and if it didn't match try next combination
    use text file size to realize the length of main text file instead of asking user
"""

import itertools
import os
from filehash import FileHash


# set the length of the secret
# by experiment you can see a txt file with n characters is n bytes!
file_size = os.path.getsize('main.txt')
n = file_size

# read alphabet file
with open('alpha.txt', 'r') as f:
    alphabet = f.read().strip()

# calculate hash of main file using sha512
sha512hasher = FileHash('sha512')
main_hash = sha512hasher.hash_file("main.txt")

# generate a possible combination and check the hash if that was not match the main hash try next
guess_num = 0
for c in itertools.product(alphabet, repeat=n):
    # generate guess secret
    guess_secret = ''.join(c)

    # write guess secret to file
    with open('guess.txt', 'w') as f:
        f.write(guess_secret)
        f.close()
    # get hash of guess secret
    guess_hash = sha512hasher.hash_file("guess.txt")

    # increment guess counter
    guess_num += 1

    # check if guess hash matches main hash
    if guess_hash == main_hash:
        print(f"Match found after {guess_num} guesses! : {guess_secret}")
        break
    else:
        print(f"Guess #{guess_num}: {guess_secret} ({guess_hash})")
