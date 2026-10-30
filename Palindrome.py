string = input("Enter a string: ")
reverse = string[::-1]
if string == reverse:
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")
