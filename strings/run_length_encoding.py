'''
Write a function that takes in a non-empty string and returns its run-length encoding.
From Wikipedia, "run-length encoding is a form of lossless data compression in which runs 
of data are stored as a single data characters. So the run "AAA" would be encoded as "3A".
To make things more complicated, however, the input string can contain all sorts of 
special characters, including numbers. And since encoded data must be decodable, 
this means that we can't naively run-length-encode long runs. For example, 
the run "AAAAAAAAAAAA" (12 A), can't be encoded as "12A", since this string can be 
decoded as either "AAAAAAAAAAAA" OR "1AA". Thus, long runs(runs of 10 or more characters)
should be encoded in a split fashion; the aforementioned run should be encoded as 
"9A3A"
stirng = "AAAAAAAAAAAAABBCCCCDD"
output = "9A4A2B4C2D"
'''


def runLengthEncoding(string):
    output = []
    count = 1

    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i-1]

        if curr != prev or count == 9:
            output.append(str(count))
            output.append(prev)
            count = 0
        count += 1

    output.append(str(count))
    output.append(string[len(string)-1])

    return "".join(output)


input = "AAAAAAAAAAAAABBCCCCDD"
print(runLengthEncoding(input))
