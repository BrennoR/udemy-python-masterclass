# Rewrite the following code to use a list comprehension, instead of a for loop.
#
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).
 
text = input("Please enter your text: ")
 
output = []
for x in text.split():
    output.append(len(x))
print(output)
 
# type your solution here:

my_output_1 = [len(x) for x in text.split()]
print(my_output_1)
 
# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):
 
output = []
for x in text.split():
    output.append((x, len(x)))
print(output)
 
# type the corresponding comprehension here:

my_output_2 = [(x, len(x)) for x in text.split()]
my_output_3 = {(x, len(x)) for x in text.split()}   # sets can't contain duplicates, and also no order by definition
print(my_output_2)
print(my_output_3)
