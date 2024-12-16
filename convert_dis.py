# Question:
"""Write program to convert the distance (in feet) to inches, yards, and miles. 
Input: 
Enter the distance in feet : 5
Expected Output:
Distance in feet : 5.0 
Distance in inches : 60.0
Distance in yards : 1.6666666666666667 
Distance in miles : 0.000946969696969697 """

feet = float(input("Enter the distance in feet: "))
inches = feet * 12
yards = feet / 3
miles = feet / 5280
print(f"Distance in feet: {feet}")
print(f"Distance in inches: {inches}")
print(f"Distance in yards: {yards}")
print(f"Distance in miles: {miles}")

