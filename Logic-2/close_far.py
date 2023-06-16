def close_far(a, b, c):
  condition_1 = abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >= 2
  condition_2 = abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b) >= 2
  return condition_1 or condition_2