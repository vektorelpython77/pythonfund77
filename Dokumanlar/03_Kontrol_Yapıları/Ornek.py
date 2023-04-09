from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import random as rnd
print("".join([rnd.choice(rnd.choice([ascii_lowercase,\
                                      ascii_uppercase,\
                                        digits,\
                                        punctuation])) for i in range(20)]))