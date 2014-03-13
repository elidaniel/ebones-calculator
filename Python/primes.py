# vim:encoding=utf-8:ts=2:sw=2:expandtab


# Start prime generation at 3 and skip all even numbers 
# because even numbers after 2 are never prime.
_prime_cache = [2,3]

# Will add to internal cache of prime number and return a list of those primes
def generate_primes(max):
  # Convert max argument to integer
  max = int(max)
  
  # Start 2 after the last prime generated and skip each even number.
  # This assumes that the last prime is odd (which is why we seed it with [2,3].
  for n in range(_prime_cache[-1]+2, max+1, 2):
    
    # A number is prime only if no other primes divide into it.
    for p in _prime_cache:
      
      # If the current number we are checking is divisable by the
      # current prime we are checking it against with no remainder
      # then this is NOT a prime.
      if n % p == 0:
        break
    
    # woo hoo, we got to the end and did not break
    else:
      _prime_cache.append(n)
    
  # Return a list of the primes up to the max.
  return [p for p in _prime_cache if p <= max]


 
  
  
def prime_factor(n):
  
  factors = []
  
  # Get all the primes up to the square root of the number in question
  primes = generate_primes(n**.5)
  
  # Check all primes until a hit is found.  Then add that prime as a
  # factor and divide the number by the prime.  Repeat until no primes
  # are hit, at which point we know that the remaining number is a prime
  while True:
    for p in primes:
      if n % p == 0:
        factors.append(p)
        n = n // p
        if n == 1:
          return factors
        else:
          break
    else:
      factors.append(n)
      return factors
  
    
 
  
  





if __name__ == '__main__':
  print(generate_primes(100))
  

