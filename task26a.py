#task26a
variable1 = True
variable2 = False
variable3 = False
variable4 = False
result = variable1 or variable2 or variable3 or variable4
print("Result:", result)
#The or operator returns True if at least one of the operands is True.
#In this case, variable1 is True, so the result of the entire expression is True
#The other variables (variable2, variable3, and variable4) are not even evaluated
#after the first True is encountered because the result is already determined by the presence of True in the expression.
