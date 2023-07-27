# For loop Basic 1

#? 1. Print all integers from 0 - 150
for i in range(0,151):
    print (i)

#? 2. Print all the multiples of 5 from 5 - 1000
# start, stop, step
for i in range(5, 1001, 5):
    print(i)

#? 3. Counting the Dojo Way
#? Print all integers from 1 - 100. 
#? If divisible by 5 print "Coding"
#? If divisible by 10 print "Coding Dojo"
#* What happens when we put 5 first?
# If you do modulus by 5 first, then all of the values that are divisible by 5 will be printed. However, if you do modulus by 10 first, then all of the values that are divisible by 10 will be printed. Since there are no values that are divisible by 10 that are also divisible by 5, then Coding Dojo will never be printed.
for i in range(1, 101):
    if i % 10 == 0:
        print('Coding')
    elif i % 5 == 0:
        print('Coding Dojo')
    else: 
        print(i)

#? 4. Whoa that sucker's huge. Add odd integers from 0 - 500,000 and print the final sum
sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)
# Output: 62,500,000,000

#? 5. Countdown by 4's
#? Print positive numbers, starting at 2018, counting down by 4
for i in range(2018, 0, -4):
    print(i)

#? 6. Flexible Counter
#? Set three variables: low_num, high_num, and mult
#? starting at low_num and going through high_num
#? print only the integers that are a multiple of mult
#? Ex. low_num = 2, high_num = 9, mult=3
#? Should print 3, 6, 9 on successive lines
low_num = 2
high_num = 9
mult = 3

for i in range(low_num, high_num+1): # to get the last value (high_num) we must go beyond it by 1!
    if i % mult == 0:
        print(i)
