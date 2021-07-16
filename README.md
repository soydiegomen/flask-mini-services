# Flask Mini Services
Proyecto para hacer pruebas rapidas con python + flask + ORM

### Instalar ambiente virtual
virtualenv venv

### Instalar dependencias
pip3 install -r requirements.txt

### Levantar el servidor
python3 app.py

### Actualizar la BD
python3 models.py


### Agregar usuarios SQLite
from models import User
from app import db
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
User.query.all()

### Endpoints

+Obtiene la lista de usuarios
http://127.0.0.1:5000/

+Crear un nuevo usuario
http://127.0.0.1:5000/create_user

+Create notes
http://127.0.0.1:5000/create_note