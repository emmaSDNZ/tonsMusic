comandos iniciales

pip install requests

pip install virtualenv
pip install SQLAlchemy
pip install cryptography
pip install pymysql
pip install uvicorn fastapi   
pip freeze > requirements.txt


. venv\scripts\activate   <-- activa entorno virtual para windows

uvicorn main:app --reload  <-- ejecuta el servidor



COMANDOS cli base de datos:
co
mysql -u root -p
create database disqueria;

show databases;
use disqueria
select * from users;


