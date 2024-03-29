'''
Write a function that takes in a string of one or more words, and returns 
the same string, but with all five or more letter words reversed 
(like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
Examples:

spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
spinWords("This is a test") => "This is a test" 
spinWords("This is another test") => "This is rehtona test"
'''


def spin_words(sentence):
    words = sentence.split(' ')
    res = []

    for word in words:
        if len(word) >= 5:
            flip = ''.join(reversed(list(word)))
            res.append(flip)
        else:
            res.append(word)
    return ' '.join(res)


def spin_words_alt(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(' ')])


sentence = "Hey fellow warriors"

print(spin_words(sentence))
print(spin_words_alt(sentence))
