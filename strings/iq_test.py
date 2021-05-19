'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Examples:
iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

'''


def iq_test(nums):
    even_count, odd_count = 0, 0
    evens, odds = 0, 0

    arr = nums.split()

    for i, el in enumerate(arr):
        if int(el) % 2 == 0:
            even_count += 1
            evens = i
        else:
            odd_count += 1
            odds = i

    if even_count == 1:
        return evens + 1
    else:
        return odds + 1


def iq_alt(nums):
    n = [int(i) % 2 for i in nums.split()]
    if n.count(0) > 1:
        return n.index(1) + 1
    else:
        return n.index(0) + 1


numbers = "2 4 7 8 10"
print(iq_test(numbers))
print(iq_alt(numbers))
