List1 = (['apple', 'banana', 'blueberry', 'banana', 'blueberry', 'coconut', 'blueberry', 'coconut', 'lemon', 'mango'])
List2 = (['melon', 'banana', 'pineapple', 'banana', 'melon', 'coconut', 'watermelon', 'coconut', 'watermelon', 'orange'])
Common = []
for element in List1:
    if element in List2:
        Common.append(element)

print(Common)