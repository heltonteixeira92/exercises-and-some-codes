string = 'ABCDCDC'
sub_string = 'CDC'

count = 0
for i in range(len(string)):
    print(string[i:i + len(sub_string)])
    if string[i:i+3] == sub_string:
        count += 1

print(count)
