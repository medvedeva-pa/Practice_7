def is_palindrome(s):
    rev_s = s[::-1]
    if rev_s == s:
        return True
    else:
        return False

print(is_palindrome('довод'))