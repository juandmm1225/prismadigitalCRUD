# prismadigitalCRUD

# Primero, crear un entorno virtual y activarlo:

python -m virtualenv env
.\venv\Scripts\activate o cd hasta llegar al directorio y .\activate

# Crear un archivo .env (en la raíz del proyecto) para las variables de entorno:

SECRET_KEY=SECRET_KEY
PGSQL_HOST=host
PGSQL_USER=user
PGSQL_PASSWORD=password
PGSQL_DB=database

# Librerías usadas:

pip install flask_httpauth
pip install flask flask-cors psycopg2 python-decouple python-dotenv

# Correr el script en la base de datos.

CREATE TABLE users ( id serial NOT NULL, username varchar(50), password varchar(500), email
varchar(100) );
CREATE TABLE bill ( id serial, date_bill date, user_id integer, value numeric(9), type integer,
observation varchar(120) );
ALTER TABLE users ADD CONSTRAINT PK_user PRIMARY KEY (id) ;
ALTER TABLE bill ADD CONSTRAINT PK_bill PRIMARY KEY (id) ;
ALTER TABLE bill ADD CONSTRAINT FK_bill_user FOREIGN KEY (user_id) REFERENCES users (id) ON
DELETE No Action ON UPDATE No Action ;

# Correr el proyecto.

python .\src\app.py 

# Prueba API.

En el directorio principal se adjunta la colección de Postman para hacer la prueba de los servicios.
