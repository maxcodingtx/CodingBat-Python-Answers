def near_hundred(n):
  diff_100 = abs(100-n)
  diff_200 = abs(200-n)
  if 10 >= diff_100 or 10 >= diff_200:
    return True
  return False
