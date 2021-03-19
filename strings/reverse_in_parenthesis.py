'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''


def reverseInParentheses(str):

    for i in range(len(str)):
        if str[i] == "(":
            start = i
        if str[i] == ")":
            end = i
            return reverseInParentheses(str[:start] + str[start+1:end][::-1]+str[end+1:])
    return str


input = "foo(bar)baz"

print(reverseInParentheses(input))
