str = input("enter a palindrome  ")
palindrome=("")
for i in range(len(str)-1,-1,-1):
    palindrome+=str[i]

if palindrome==str:
    print("its a palindrome")
else:
    print("it not a palindrome")