'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''
ans:
# Get input from the user
birth_year_last_two_digits = int(input("Enter the last 2 digits of your birth year: "))
current_year_last_two_digits = int(input("Enter the last 2 digits of the current year: "))

# Calculate the birth year and current year
current_year_full = 2000 + current_year_last_two_digits if current_year_last_two_digits >= 0 else 1900 + current_year_last_two_digits
birth_year_full = 2000 + birth_year_last_two_digits if birth_year_last_two_digits >= 0 else 1900 + birth_year_last_two_digits

# Calculate age
age = current_year_full - birth_year_full

# Output the age
print(age)
