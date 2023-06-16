def count_code(str):
  code_count = 0
  for i in range(0, len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      code_count += 1
  return code_count