# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it


fib = [0, 1]


for idx, f in enumerate(fib):
    if idx <= 50:
        last = fib[-1]
        second_to_last = fib[-2]
        new_number = last + second_to_last
        fib.append(new_number)
        # print(fib)
        print(f'term: {idx} / number: {new_number}')
    else:
        break


# for f, idx in enumerate(fib):
#     if idx <= 50:
#         print(f'term: {idx} / number: {f}')
#     else:
#         break


# print(last, second_to_last)

