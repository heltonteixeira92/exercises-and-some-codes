n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores


query_name = input()
values = student_marks[query_name]
count = len(values)
print(f'{sum(values)/count:.2f}')
