string = input("Enter String: ")

word_list = str.split(string.lower())

word_dict = {}
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

list_of_words = sorted(word_dict.keys())

word_length = []
for word in word_dict:
    word_length.append(len(word))

spacing = max(word_length)

for word in list_of_words:
    print("{:<{}}: {}".format(word, spacing+1, word_dict[word]))
