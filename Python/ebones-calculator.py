# vim:encoding=utf-8:ts=2:sw=2:expandtab


###############################################################################
def GetMenuChoice(): 
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  while True:
    print()
    print('(a) - addition')
    print('(s) - subtraction')
    print('(m) - multiplication')
    print('(d) - division')
    print('(dr) - divesion remanders')
    print('(e) - exit')
    print()
    text = input('Enter type of problem: ')

    if text not in ('a', 's', 'm', 'd', 'e' 'dr'):
      print()
      print('Error: invalid input')
      continue
    pass#if

    return text

  pass#while
pass#def


###############################################################################
def input_int(text):
  val = None
  count = 0
  while val is None:
    count += 1
    try:
      val = int(input(text + ': '))
    except ValueError as e:
      print(e) 
      if count == 2:
        print('Come on man')
      elif count == 3:
        print('Are you smart?')
      elif count == 4:
        print('Are you 3 years old???')
      elif count >= 5:
        print('You are offficially a retarrrrdddooo')
      elif count >= 6:
        print('Where you born last night?!?')
    
  return val


###############################################################################
def Addition():
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  
  aug = input_int('Enter Augend')
  add = input_int('Enter Addend')

  ans = aug + add
  
  print()
  print('ANSWER: {0} + {1} = {2}'.format(num, aug, add))
  print()
  input('Press Enter')
  
  return

###############################################################################
def Subtraction():
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  
  sub = input_int('Enter Subtrahend')
  min = input_int('Enter Minuend')

  ans = min - sub
  
  print()
  print('ANSWER: {0} - {1} = {2}'.format(sub, min, ans))
  print()
  input('Press Enter')
  
  return




###############################################################################
def Multiplication():
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  
  mul = input_int('Enter Multiplicand')
  mul = input_int('Enter Multiplier')

  ans = mul * mul
  
  print()
  print('ANSWER: {0} x {1} = {2}'.format(num, mul, mul))
  print()
  input('Press Enter')
  return


################################################################################



def Division():
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  
  div = input_int('Enter Dividend')
  div = input_int('Enter Divisor')

  ans = div / div

  print()
  print('ANSWER: {0} % {1} = {2}'.format(div, div, ans))
  print()
  input('Press Enter')
  return



################################################################################



def Division_remander():
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  
  div = input_int('Enter Dividend')
  div = input_int('Enter Divisor')

  ans = div // div
  
  print()
  print('ANSWER: {0} // {1} = {2}'.format(div, div, ans))
  print()
  input('Press Enter')
  
  return
###############################################################################
while True:

  pt = GetMenuChoice()
  print(pt)
  if pt == 'e':
    break

  elif pt == 'a':
    Addition()

  elif pt == 's':
    Subtraction()

  elif pt == 'm':
    Multiplication()
    
  elif pt == 'd':
    Division()

  elif pt == 'dr':
    Division_renamder()



pass#while
