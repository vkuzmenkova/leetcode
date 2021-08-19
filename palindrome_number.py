def isPalindrome(x: int) -> bool:
    return True if str(x) == str(x)[::-1] else False

print(isPalindrome(121))
print(isPalindrome(90))
