def truncate(string, width):
    if len(string) > width:
        string = string[:width] + '.' + string[width:]
    return string


print("{}".format(truncate("1000", 2)))
# >> 10.00
# a = truncate('1000', 3)

