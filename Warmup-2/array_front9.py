def array_front9(nums):
  if len(nums) < 4:
    if 9 in nums:
      return True
  
  for num in nums:
    if 9 in nums[:4]:
      return True
  return False
