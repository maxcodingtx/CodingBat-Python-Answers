def front_back(str):
  
  if len(str) < 2:
    return str
  
  first_char = str[0]
  middle = str[1:-1]
  last_char = str[-1]
  
  return last_char + middle + first_char
