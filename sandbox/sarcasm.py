import random
sentence = input('sentence: ')
print(''.join(c.upper() if random.randint(0, 1) else c.lower()
              for c in sentence))
