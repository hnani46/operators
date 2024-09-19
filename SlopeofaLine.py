...
 Finding the Slope of a Line
Problem Statement
Ajay and Binoy are curious about the slope of the line joining their houses. Given the coordinates of the 2 endpoints of a line (x1,y1)(x_1, y_1)(x1​,y1​) and (x2,y2)(x_2, y_2)(x2​,y2​), write a Python program to find the slope of the line.
...
Sample Input

1
2
3
6

Sample Output

The slope of the line joining Ajay's house and Binoy's house is 2.00

Solution

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 != x1:
    slope = (y2 - y1) / (x2 - x1)
    print(f"The slope of the line joining Ajay's house and Binoy's house is {slope:.2f}")
else:
    print("The line is vertical, slope is undefined")

