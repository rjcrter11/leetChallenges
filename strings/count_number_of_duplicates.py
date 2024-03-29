'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''


def duplicate_count(s):

    count = 0
    d = {}

    for char in s.lower():
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    for x in d:
        if d[x] > 1:
            count += 1
    return count


string = "ABBA"
print(duplicate_count(string))


def count_dups_alt(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


print(count_dups_alt(string))
