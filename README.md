# StudyApp
Proyect for proyect administration

## Como instalarlo?

1. Instala python
2. Abre la terminal ya sea powershell, cmd, terminal de windows.
3. Instala django usando el siguiente comando `pip install django`
4. Abre la carpeta donde se encuentra el proyecto y escribe lo siguiente `python manage.py runserver`
5. En la parte de urls del navegador escribe `localhost:8000`

solo existen estas urls:
seleccionar usuario a registrar: `localhost:8000/users/select/`,
registrar maestro: `localhost:8000/users/maestro/`,
login: `localhost:8000/users/login/`,
saber quien esta logeado: `localhost:8000/users/whoami`,
