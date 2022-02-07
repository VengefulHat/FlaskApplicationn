Żeby uruchomić projekt:
- musisz mieć zainstalowany python (w wersji 3.x (najlepiej wyższy niż 3.6)
- zastosuj: py -m pip install flask, flask_restful, flask_wtf, flask_sqlalchemy, wtforms, wtforms.validators, flask_bcrypt, flask_ligin, email_validatior
- przejź do: /Flask_APP/
- wykonaj komendę: py app.py


Otworzy sie strona logowania!
Możesz stworzyć konto (do url dołącz: /rejestracja_1e8a9ae72c905a68d6de2c30)
Aby ominąć logowanie przejdź: /home (do url)


Fajnie jest jak widać że działa, dodałem więc moje testowe programy
Odpytywanie stron (głównch) po HTTP:
- wykonaj komendę: py http_200.py (po api program zacznie wysyłać do aplikacji wyniki z odpytywania)

Odpytywanie wszystkich podstron jakie znajdzie program (celuje głównie w zawartość href=""):
- wykonaj komendę: py req_all.py (po api program zacznie wysyłać do aplikacji wyniki z odpytywania)

