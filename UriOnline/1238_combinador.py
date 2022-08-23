# quantity = int(input())

first_str, second_str = str(input()).split()

first_list = [x for x in first_str]
second_list = [x for x in second_str]

zipped = zip(first_list, second_list)

zipped_list = list(zipped)

string = ''.join(str(zipped_list))

string_replaced = string.replace('[', '').replace(']', '').replace('(', '').replace(',', '').replace(')', '').replace(
    "'", "").replace(' ', '')

print(string_replaced)
