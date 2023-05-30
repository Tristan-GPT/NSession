import random

caracteres = [
  
    "1","2","3",

    "4","5","6","7","8","9","0",

  ]

def pluginid_gen():

    token = ''
    
    for i in range(18):
      
      token = f"{token}{random.choice(caracteres)}"

    return token  