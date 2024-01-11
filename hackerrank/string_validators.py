s = 'qA2'

result = {'isalnum': False,
          'isalpha': False,
          'isdigit': False,
          'lower': False,
          'upper': False
          }

for char in s:

    if char.isalnum():
        result['isalnum'] = True

    if char.isalpha():
        result['isalpha'] = True

    if char.isdigit():
        result['isdigit'] = True

    if char.islower():
        result['lower'] = True

    if char.isupper():
        result['upper'] = True

for value in result.values():
    print(value)