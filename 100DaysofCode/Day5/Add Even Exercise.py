"""
Create a code that calculate the sum of all terms from a given sequence.
"""
# all numbers from 0 to 100
s1 = 0
for item in range(0, 101):
    s1 += item
print(s1)

# even numbers from 0 to 100
s2 = 0
for item in range(0, 101):
    if item % 2 == 0:
        s2 += item
print(s2)

# even numbers from 0 to 100 - vers.2.0
s22 = 0
for item in range(0, 101,2):
    s22 += item
print(s22)

# odd numbers from 0 to 100
s3 = 0
for item in range(0, 101):
    if item % 2 != 0:
        s3 += item
print(s3)
