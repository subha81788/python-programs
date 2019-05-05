def reverse_number(n):
    if not n:
        raise ValueError("Number can't be null or empty")
    n1=0
    while n > 0:
        d=n%10
        n=n//10
        n1=n1*10+d
    return n1

def check_palindrome(n):
    return n == reverse_number(n)

if __name__ == "__main__":
    numbers = [123,456,789,454,878,987,765]
    palindromes=[]
    for n in numbers:
        if check_palindrome(n):
            palindromes.append(n)
    print(palindromes)
