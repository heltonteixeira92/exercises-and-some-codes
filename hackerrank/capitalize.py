def solve(s):
    string_list = list(s.split())
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    title_list = []
    for word in string_list:
        if word[0] not in numbers:
            word = word.title()
        title_list.append(word)

    string = ' '.join(title_list)   
    return str(string)


if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)




# def solve(s):
#     string_list = s.split()
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     title_list = []
#     for word in string_list:
#         if word[0] not in numbers:
#             word = word.title()
#         title_list.append(word)
#
#     return ' '.join(title_list)
#
#
# if __name__ == '__main__':
#
#     s = input()
#
#     result = solve(s)
#
#     print(s)
