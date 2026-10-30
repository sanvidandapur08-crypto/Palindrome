import sys
# Get string from command-line argument
string = sys.argv[1]
# Reverse the string
reverse = string[::-1]
# Check palindrome
if string.lower() == reverse.lower():
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")
