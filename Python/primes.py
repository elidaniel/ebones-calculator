# vim:encoding=utf-8:ts=2:sw=2:expandtab

def generate_primes(max):
  primes = [2]
  
  # Start prime generation at 3 and skip all even numbers 
  # because even numbers after 2 are never prime.
  for n in range(3,max,2):
    
    # A number is prime only if no other primes divide into it.
    for p in primes:
      
      # If the current number we are checking is divisable by the
      # current prime we are checking it against with no remainder
      # then this is NOT a prime.
      if n % p == 0:
        break
    
    # woo hoo, we got to the end and did not break
    else:
      primes.append(n)
    
  
  return primes


  





if __name__ == '__main__':
  print(generate_primes(100))


