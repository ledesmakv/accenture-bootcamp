def count_repeated_chars(string, character):
    count = 0
    for i in string:
        if i == character:
            count += 1
    return count

print(count_repeated_chars('hola este es un texto aeiou', 'q'))
print(count_repeated_chars('hola este es un texto aeiou', 'e'))

def count_char(word, char):
    count = 0
    if char in word:
        for c in word:
            if c == char:
                count += 1
                return count
            else:
                return False

def count_char2(word, char):
    count = word.count(char)
    if count == 0:
        return False
    else:
        return count

test_1 = count_repeated_chars('hola este es un texto aeiou', 'q')
test_2 = count_repeated_chars('hola este es un texto aeiou', 'e')

assert test_1 == 2
assert test_2 == False
