'''
5) 
Write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.
  Student Type  
  Student Type denoted as  
  Fee Details  
Merit Seat Day Scholar
MSDS

Tuition fee + Bus fee



Merit Seat Hosteller
MSH
Tuition fee + Hostel fee

Management Seat Day Scholar



MGSDS

150% of Tuition fee + Bus fee



Management Seat Hosteller
MGSH

150% of Tuition fee + Hostel fee




Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
Output format:
Print the total fee amount of the corresponding student with 2 decimal places.
Refer below sample output for formatting
Sample Input:
MSH
40000
50000
Sample Output:
90000.00
'''
ans:
def calculate_fee(student_type, tuition_fee, additional_fee):
    # Convert input values to float
    tuition_fee = float(tuition_fee)
    additional_fee = float(additional_fee)

    if student_type == "MSDS":
        # Merit Seat Day Scholar
        total_fee = tuition_fee + additional_fee
    elif student_type == "MSH":
        # Merit Seat Hosteller
        total_fee = tuition_fee + additional_fee
    elif student_type == "MGSDS":
        # Management Seat Day Scholar
        total_fee = 1.5 * tuition_fee + additional_fee
    elif student_type == "MGSH":
        # Management Seat Hosteller
        total_fee = 1.5 * tuition_fee + additional_fee
    else:
        return "Invalid student type"

    # Print the total fee amount formatted to 2 decimal places
    return f"{total_fee:.2f}"

# Input
student_type = input().strip()
tuition_fee = input().strip()
additional_fee = input().strip()

# Calculate and print the fee
print(calculate_fee(student_type, tuition_fee, additional_fee))
