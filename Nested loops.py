#Asking user for the upper bound

upper_bound = int(input("Enter an upper bound for an check: "))

deficient = 0
perfect = 0
abundant = 0

#Using for loop to get the range between 1 and 20 including the upper bound. i.e Adding 1 to upper bound

for i in range (1, upper_bound+1):
  divisor_sum = 0
  for j in range (1,i):
    if i % j == 0:
      divisor_sum += j
      
# Checking the condition mentioned in the question to get the numbers of deficienf, perfect, and abundant numbers.
      
  if divisor_sum < i:
    deficient += 1
  elif divisor_sum == i:
    perfect += 1
  elif divisor_sum > i:
    abundant +=1

#Using f string to make it easy along with the ""\n" to break the line.
    
print(f"Between 1 and {upper_bound} there are \n{deficient} deficient numbers \n{perfect} perfect numbers \n{abundant} abundant numbers")
