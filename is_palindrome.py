def is_palindrome(s):
    return s == s[::-1]


s = "madam"
print("Is palindrome:", is_palindrome(s))
s = "hello"
print("Is palindrome:", is_palindrome(s))
