def ispalindrome(s):

    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in 'abcdefghijklmnopqrstuvwxyz':
            ans = ans + c
            return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))

print('Is "LUZA ROCELINA, A NAMORADA DO MANUEL, LEU NA MODA DA ROMANA: ANIL E COR AZUl" a palindrome?')
print(ispalindrome('eve'))