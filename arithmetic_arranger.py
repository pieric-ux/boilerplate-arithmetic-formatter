import re

def arithmetic_arranger(problems, showResult=False):
  valid_operator = ('+', '-')
  space_between = 4*' '
  count = 0
  top = ''
  bottom = ''
  dashes = ''
  tot = ''

  if(len(problems) > 5):
    return("Error: Too many problems.")
  
  for problem in problems:
    count += 1
    problem = problem.split()
    operand_1 = problem[0]
    operator = problem[1]
    operand_2 = problem[2]
    
    if (operator not in valid_operator):
      return("Error: Operator must be '+' or '-'.")
      
    if (not re.search("^[0-9]*$", operand_1) or not re.search("^[0-9]*$", operand_2)):
      return('Error: Numbers must only contain digits.')

    if (len(operand_1) > 4 or len(operand_2) > 4):
      return("Error: Numbers cannot be more than four digits.")

    if len(operand_1) > len(operand_2):
      nChar = len(operand_1) + 2
    else:
      nChar = len(operand_2) + 2

    if (operator == '+'):
      result = int(operand_1) + int(operand_2)
    else:
      result = int(operand_1) - int(operand_2)

    if (count == len(problems)):
      top += (nChar - len(operand_1)) * ' ' + operand_1
      bottom += operator + (nChar - 1 - len(operand_2)) * ' ' + operand_2
      dashes += nChar * "-"
      
      if (showResult):
        tot += (nChar - len(str(result))) * ' ' + str(result)
      else:
        tot = ''
        
    else:
      top += (nChar - len(operand_1)) * ' ' + operand_1 + space_between
      bottom += operator + (nChar - 1 - len(operand_2)) * ' ' + operand_2 + space_between
      dashes += nChar * "-" + space_between

      if (showResult):
        tot += (nChar - len(str(result))) * ' ' + str(result) + space_between
      else:
        tot = ''
        
  if (tot == ''):
    return (top + '\n' + bottom + '\n' + dashes)
  else:
    return (top + '\n' + bottom + '\n' + dashes + '\n' + tot)