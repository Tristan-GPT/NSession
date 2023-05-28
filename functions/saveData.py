from classes.Session import Session
from environments.session import session

def saveData(session_index, data_index, newData):
    try:
        if session_index >= 0 and session_index < len(session):
            sess = session[session_index]
            data = sess['data']
            if data_index >= 0 and data_index <= len(data):
                data.insert(data_index, newData)
            else:
                raise ValueError("L'index des données spécifié est invalide.")
        else:
            raise ValueError("L'index de la session spécifiée est invalide.")
    except IndexError:
        raise ValueError("Une erreur d'index est survenue.")
    except Exception:
        raise ValueError("Une erreur est survenue lors de la sauvegarde des données.")