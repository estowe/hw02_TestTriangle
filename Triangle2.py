#!/bin/python3
def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'Input greater than 200'

    elif a <= 0 or b <= 0 or c <= 0:
        return 'Input less than 0'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    elif not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'Input not integer'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    elif (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    elif a == b or b == c or c == b:
        return 'Isoceles'
    else:
        return 'Not a defined triangle' 
    
import sys

class InvalidTriangleError(Exception): #Thank you ChatGPT for this contribution!
    pass

if len(sys.argv) == 4: 
    input_side1 = int(sys.argv[1])
    input_side2 = int(sys.argv[2])
    input_side3 = int(sys.argv[3])

    try:
        process_results = classifyTriangle(input_side1, input_side2, input_side3)
        print(process_results) 
    except InvalidTriangleError as e: #Thank you ChatGPT for this contribution!
        print(f"I'm sorry, but one of your sides is not a valid entry.\n{str(e)}")
