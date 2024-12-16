"""With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
Note:
Use set() to store a number of values without duplicate.
Expected Output:
[12, 24, 35, 88, 120, 155]"""

lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
result = []
seen = set()
for num in lst:
    if num not in seen:
        result.append(num)
        seen.add(num)
print(result)
