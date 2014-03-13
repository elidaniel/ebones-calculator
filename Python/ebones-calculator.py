# vim:encoding=utf-8:ts=2:sw=2:expandtab

from primes import generate_primes

###############################################################################
def GetMenuChoice(): 
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  while True:
    print()
    print('(a)  - addition')
    print('(s)  - subtraction')
    print('(m)  - multiplication')
    print('(d)  - division')
    print('(dr) - divesion remanders')
    print('(pl) - prime number list')
    print('(e)  - exit')
    print()
    text = input('Enter type of problem: ')

    if text not in ('a', 's', 'm', 'd', 'e', 'dr', 'pl'):
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
  
  Augend = input_int('Enter Augend')
  Addend = input_int('Enter Addend')

  ans  =  Augend + Addend      
  
  print()
  print('ANSWER: {0} + {1} = {2}'.format(num, Augend, Addend))
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
  
  multiplicand = input_int('Enter Multiplicand')
  multiplier = input_int('Enter Multiplier')

  ans = multiplicand * multiplier
  
  print()
  print('ANSWER: {0} x {1} = {2}'.format(num, multiplicand, multiplier))
  print()
  input('Press Enter')
  return

################################################################################
def Division():
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  
  dividend = input_int('Enter Dividend')
  divisor = input_int('Enter Divisor')

  ans = dividend / divisor

  print()
  print('ANSWER: {0} / {1} = {2}'.format(dividend, divisor, ans))
  print()
  input('Press Enter')
  return

################################################################################
def Division_remainder():
  '''
  This function will prompt the user to input a valid problem type and then
  return that problem type.
  '''
  
  dividend  = input_int('Enter Dividend')
  divisor = input_int('Enter Divisor')

  ans = dividend // divisor
  rem = dividend % divisor

  print()
  print('ANSWER: {0} / {1} = {2} R{3}'.format(dividend, divisor, ans, rem))
  print()
  input('Press Enter')
  return

###############################################################################
def Prime_List():
  '''
  This function will generate a list of prime numbers
  '''
  
  max = input_int('Biggest prime number? ')
  
  primes = generate_primes(max)
  
  print()
  print('Primes <= {0}: {1}'.format(max, list(primes)))
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
    Division_remainder()

  elif pt == 'pl':
    Prime_List()


pass#while
