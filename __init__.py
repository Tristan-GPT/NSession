import random

caracteres = [
  
    "A", "B", "C","D","E","F",

    "G","H","I","J","K","L","M",

    "N","O","P","Q","R","S","T",

    "U","V","W","X","Y","Z","a","b",

    "c","d","e","f","g","h","i","j","k",

    "l","m","n","o","p","q","r","s","t",

    "u","v","w","x","y","z","1","2","3",

    "4","5","6","7","8","9","0",

  ]

session = []
  
  
def sessiontoken_gen():

    password = ''
    
    for i in range(100):
      
      password = f"{password}{random.choice(caracteres)}"

    return password  

class Session:
    def createSession(self, name = str, id = int):
        self.name = name
        self.id = id
        self.sessionToken = sessiontoken_gen()
        self.data = []
        session.insert(0, {"name": self.name, "id": self.id, "sessionToken": self.sessionToken, 'data': []})

ses = Session()
ses.createSession(name="session1", id="session1-user-data")

def saveData(newData):
  try:
     sess = session[0]
     data = sess['data']
     data.insert(0, newData)
     print(data)
     
  except:
    print("Error")
