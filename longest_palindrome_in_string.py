#15TH SOLUTION
def check_palindrome(string):
    reversed_string = string[::-1]
    status = True
    if(string!=reversed_string):
        status = False
    return status
string = input("Enter a string: ")
n = len(string)
lenght = 0
if(check_palindrome(string)):
    print("Longest Palindrome = ",string)
else:
    for i in range(n):
        for j in reversed(range(n)):
            if(j>=i):
                check = check_palindrome(string[i:j+1])
                if (check) and (lenght < len(string[i:j+1])) :
                    lenght  = len(string[i:j+1])
                    longest = string[i:j+1]
    print("Longest Palindrome = ",longest)
