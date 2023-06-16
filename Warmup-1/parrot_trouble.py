def parrot_trouble(talking, hour):
  if talking == True:
    return 7 > hour or 20 < hour
  return False
