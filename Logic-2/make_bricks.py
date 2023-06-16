def make_bricks(small, big, goal):
  
  big = big * 5
  
  if goal % 5 == 0 and big >= goal:
      return True
  if small + big < goal or goal % 5 > small:
      return False
  return True
