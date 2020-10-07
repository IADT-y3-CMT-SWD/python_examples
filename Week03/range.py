# range.py
numbers = list(range(1,6))
print('numbers using range')
print(numbers)
print('=======================')
print('odd numbers using range')
odd_numbers = list(range(1,200,2))
print(odd_numbers)
print('=======================')
print('backward numbers using range')
bw_numbers = list(range(100,1,-5))
print(bw_numbers)
print('=======================')

# Print a message five times.
for x in range(5):
    print('Hello world!:  {}'.format(x))