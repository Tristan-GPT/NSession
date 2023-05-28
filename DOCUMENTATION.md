# Documentation PyIronSession V0.5.0

# Comment installer ?
    + En premier lieu, télécharger le code en appuyant sur "Code" puis "Download ZIP File"
    + Puis, dans votre projet, créez un dossier s'appelant "lib" puis un sous-dossier s'appelant "PyIronSession". Mettez-y le code.

# Exemple d'utilisation:
    ```py
    from lib.PyIronSession.classes.Session import Session
    from lib.PyIronSession.functions.saveData import saveData

    sess = Session()
    sess.createSession(index=0, name="session1", id="session1-user1-data", security_code="12345") # Not use 12345 for security code !

    saveData(session_index=0, data_index=0, newData="Hello")

    data = sess['data']
    print(data)

    ```    