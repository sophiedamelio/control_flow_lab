# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter the lengths of three side of a triangle: ')

length_a = int(input('a: '))
length_b = int(input('b: '))
length_c = int(input('c: '))

# triangle_lengths = [length_a, length_b, length_c]

if length_a == length_b and length_b == length_c:
    type_of_triangle = 'equalateral'

elif length_a != length_b and length_b != length_c and length_a != length_c:
    type_of_triangle = 'scalene'

else:
    type_of_triangle = 'isosceles'

print(f' A triangle with sides of {length_a}, {length_b} & {length_c} is a {type_of_triangle} triangle')
