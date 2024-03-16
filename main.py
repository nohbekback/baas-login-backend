from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Definir modelos de Login
class Login(BaseModel):
    username: str
    password: str

# Establecer datos de autenticación
login_data = {"username": "brendac123", "password": "1234"}

# Inicializar la aplicación FastAPI
app = FastAPI()

# Estructuras de datos para almacenar usuarios
#login_db = {}

# Definir rutas
@app.post("/login")
def user_login(login: Login):
    if login.username == login_data["username"] and login.password == login_data["password"]:
        return {"message": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas") 

""" @app.post("/login")
def user_login(login: Login):
    if login.username not in login_db or login_db[login.username].password != login.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful"} """
