10/2/2025

'''
Given a non-negative integer, return its binary representation as a string.
A binary number uses only the digits 0 and 1 to represent any number. 
To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder. 
Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:
12 ÷ 2 = 6 remainder 0

'''


def to_binary(decimal):
    remainder = ""
    tmp = decimal 
    while tmp > 0: 
        remainder += str(tmp % 2)
        #print(remainder)
        tmp //= 2
    
    return remainder[::-1]
    
print(to_binary(5))
print(to_binary(12))


'''
1. to_binary(5) should return "101".
2. to_binary(12) should return "1100".
3. to_binary(50) should return "110010".
4. to_binary(99) should return "1100011".
'''