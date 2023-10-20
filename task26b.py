#task26b
variable1 = True
variable2 = False
variable3 = False
variable4 = False
result = variable1 and variable2 and variable3 and variable4
print("Result:", result)
#The and operator returns False if at least one of the operands is False.
#In this case, variable1 is True, but the other variables (variable2, variable3, and variable4) are False.
#Since the and operator requires all operands to be True for the result to be True, the overall result is False.