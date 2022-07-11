print("Name- Aditya Motale")
string_input = '''Friendship ... is born at the moment when one man says to another "What! You too? I thought that no one but myself ...'''

words = string_input.split()

dictionary = {}

for word in words:

    if (word[0] not in dictionary.keys()):
        dictionary[word[0]] = []
        dictionary[word[0]].append(word)

    else:
        if (word not in dictionary[word[0]]):
            dictionary[word[0]].append(word)

dictionary