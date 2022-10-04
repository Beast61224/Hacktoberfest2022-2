n = int(input())
list_of_sentences = []
for i in range(n):
    sentence = input()
    list_of_sentences.append(sentence)

new_list = [s.replace("pi", "3.14") for s in list_of_sentences]

for i in range(n):
    print(new_list[i])
