def sum67(nums):
  
  count = True
  sum = 0
  
  for i in range(len(nums)):
    
    if nums[i] == 6:
      count = False
    elif count == False and nums[i] == 7:
      count = True
    elif count == True:
      sum = sum + nums[i]
  
  return sum
