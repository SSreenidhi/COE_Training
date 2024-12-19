""" Write a program that tries to accumulate sum of values based on the input in some dictionaries. 
Insert a try/except so that the code passes.
Sample Input:
di = {"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}
Sample Output:
Total number of puppies:130"""

di1 = {"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}
di2 = {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}
di3 = {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}
di4 = {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}

di_list = [di1, di2, di3, di4]

total_puppies = 0

for di in di_list:
    try:
        total_puppies += di.get('Puppies', 0)
    except Exception as e:
        print(f"Error: {e}")

print(f"Total number of puppies: {total_puppies}")
