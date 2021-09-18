sum = 0
# start from 3 because it is the smallest multiplier of 3, to 999 which is less than 1000
for i in range(3, 1000):
  # if the number is multiplier of both 3 and 5 (like 15)
  # add it and skip the code after it, so it is not added twice.
    if i %3 == 0 and i%5==0:
        sum+=i
        continue 
      
    # a multiplier of number when divied by that number MUST has 0 reminder.
    if i % 3 == 0:
        sum+= i
    if i % 5 == 0:
        sum+= i
        
# sum = 233168
print(sum)