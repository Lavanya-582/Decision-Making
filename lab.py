'''
 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
'''
# Input the capacities of the labs and the number of students
x = int(input())  # Capacity of Lab L1
y = int(input())  # Capacity of Lab L2
z = int(input())  # Capacity of Lab L3
n = int(input())  # Number of students

# Determine which lab to allocate
suitable_labs = []

if n <= x:
    suitable_labs.append(('L1', x))
if n <= y:
    suitable_labs.append(('L2', y))
if n <= z:
    suitable_labs.append(('L3', z))

# Find the lab with the maximum capacity that can accommodate n students
if suitable_labs:
    best_lab = max(suitable_labs, key=lambda lab: lab[1])
    print(best_lab[0])
else:
    print("No suitable lab available")
