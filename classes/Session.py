from functions.sessiontoken import sessiontoken_gen
from environments.session import session

class Session:
    def createSession(self, name=str, id=str,security_code=str, index=int):
        self.name = name
        self.id = id
        self.sessionToken = sessiontoken_gen()
        self.security_code = security_code
        self.data = []

        if session and len(session) > index:
            raise ValueError("Une session existe déjà à cet index.")
        else:
            session.insert(index, {"name": self.name, "id": self.id, "sessionToken": self.sessionToken, 'data': []})
    
    def deleteSession(self, index=int):
        try:
            if index >= 0 and index < len(session):
                session.pop(index)
            else:
                raise ValueError("L'index de la session spécifiée est invalide.")
        except IndexError:
            raise ValueError("Une erreur d'index est survenue lors de la suppression de la session.")
        except Exception:
            raise ValueError("Une erreur est survenue lors de la suppression de la session.")
        
    def verifySecurityCode(self, security_code):
        if self.security_code == security_code:
            return True, self.data
        else:
            return False, None   
        