trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    """
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    """
    if len(str(us_num)) == 1:
        return trans[str(us_num)]

    elif len(str(us_num)) > 1:
        string_us_num = str(us_num)
        if string_us_num[1] == '0':
            if string_us_num[0] == '1':
                us_repr = ''
                us_repr += trans['10']
                return us_repr
            else:
                us_repr = ''
                us_repr += trans[string_us_num[0]] + ' '
                us_repr += trans['10']
                return us_repr
        elif string_us_num[0] == '1':
            us_repr = ''
            us_repr += trans['10'] + ' '
            us_repr += trans[string_us_num[1]]
            return us_repr

        else:
            us_repr = ''
            us_repr += trans[string_us_num[0]] + ' '
            us_repr += trans['10'] + ' '
            us_repr += trans[string_us_num[1]]
            return us_repr


a = convert_to_mandarin(3)
print(a)

b = convert_to_mandarin(36)
print(b)

c = convert_to_mandarin(17)
print(c)

d = convert_to_mandarin(10)
print(d)

e = convert_to_mandarin(30)
print(e)

f = convert_to_mandarin(11)
print(f)