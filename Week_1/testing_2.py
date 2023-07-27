import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1,6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Thursday' 'Wednesday', 'Friday']
day = random.choice(weekdays)
print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif day == 'Friday':
    print("OH YEAH PARTY TIME!!")
else:
    print('We are not quite there yet!')

#* Why we may see the same DAY of the week each time it runs. Try removing that day from the list.
# Some integrated development environments (IDEs) or Python interpreters might cache the results of code execution, especially for small code snippets like the one you provided. This could lead to the same output being shown repeatedly during consecutive runs within the same session.

# To ensure a fresh execution each time, try running the code in a different environment or restart the Python interpreter or IDE.