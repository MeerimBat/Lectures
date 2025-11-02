#Simple Word Counter. Write a program that asks the user for a sentence. The program should then count the occurrences of each word in the sentence
#and display the result as a dictionary.

sentence=input("Write a sentence: ")
word=sentence.lower().split()
#word = sentence.translate(str.maketrans('', '', string.punctuation))
#for word in sentence.lower().split():
   #word=word.strip(" ,.,?!")
count = {}

for i in word:
    count[i] = count.get(i, 0) + 1

print(count)



