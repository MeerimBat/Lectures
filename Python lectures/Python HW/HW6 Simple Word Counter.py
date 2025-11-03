#Simple Word Counter. Write a program that asks the user for a sentence. The program should then count the occurrences of each word in the sentence
#and display the result as a dictionary.
import string 


sentence=input("Write a sentence: ")

translator = str.maketrans('', '', string.punctuation)
word = sentence.translate(translator)
word=word.lower().split() 
print(word)

count = {}

for i in word:
    count[i] = count.get(i, 0) + 1

print(count)



