def get_unique_characters(string):
    unique_characters = []
    not_unique_characters = []
    for letter in string:
        if (letter not in unique_characters and
            letter not in not_unique_characters):
            unique_characters.append(letter)
        elif letter in unique_characters:
            unique_characters.remove(letter)
            not_unique_characters.append(letter)
    return unique_characters

#unit testing
test1 = 'lolololololz'
test2 = 'trollololololololollohehenopehaha'
test3 = 'trollololololololollohehe nopehahaa'
test4 = 'The quick brown fox jumps over the lazy dog'

print(get_unique_characters(test1))
print(get_unique_characters(test2))
print(get_unique_characters(test3))
print(get_unique_characters(test4))