# def load_words():
#     with open('words.txt') as word_file:
#         valid_words = set(word_file.read().split())
#
#     return valid_words
#
#
# if __name__ == '__main__':
#     english_words = load_words()
#     # demo print
#     print(english_words)

import numpy as np
# opening the file in read mode
my_file = open("words.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
english_words = data.split("\n")
# print(english_words)
# print(english_words[0])
number_count=0
for i in range (0,50):
    print(200*i,200*(i+1)-1)
    i=np.random.randint(200*i,200*(i+1)-1)
    print("do you know english word? Please type only \'yes\' or \'no\' ")
    print(english_words[i])
    a=input()
    if a=='yes':
        number_count=+200
for i in range (50,150):
    print(200*i,200*(i+1)-1)
    i=np.random.randint(200*i,200*(i+1)-1)
    print("do you know english word? Please type only \'yes\' or \'no\' ")
    print(english_words[i])
    a=input()
    if a=='yes':
        number_count=+200
print(number_count)