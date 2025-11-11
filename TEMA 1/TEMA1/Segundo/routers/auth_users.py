
from fastapi import APIRouter, HTTPException
#Importar JWT
import jwt
#Trabajar las excepciones de los tokens
from jwt.exceptions import InvalidTokenError
#Libreria para aplicar un hash a la contraseña
from pwdlib import PasswordHash
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

ouatha2 = OAuth2PasswordBearer(tokenUrl = "login")

#Definimos el algoritmo de encriptacion
ALGORITHM = "HS256"

#Duracion del token
ACCESS_TOKEN_EXPIRE_MINUTES = 10

# Clave que se utilizará como semilla para generar el token
# openssl rand -hex 32
SECRET_KEY = "87ab51098990feb4a2f78da9c911187a71290ebd9e98e56d8b24090815f2ce6f"

# Objeto que se utilizará para el cálculo del hash y
# la verificación de las contraseñas
password_hash = PasswordHash.recommended()

router = APIRouter()
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password:str

users_db = {
    "jlcordero": {
    "username" :  "jlcordero",
    "fullname" : "Jose Luis Cordero Fuentes",
    "email" : "jlcordero7488@gmail.com",
    "disabled" : False,
    "password" : "12345"
    }
}

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    # Miramos si el usuario existe en la Base de Datos
    user_db = fake_users_db.get(form.username)
    # Si no está en la base de datos se lanza una excepción
    if not user_db:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    # Si está, creamos un objeto de tipo UserDB a partir de su información
    user = UserDB(**fake_users_db[form.username])
    # Comprobamos que las contraseñas coinciden con verify
    if not password_hash.verify(form.password, user.hashed_password):
        # Si no coinciden lanzamos excepción
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    # Tomamos la hora actual + el tiempo de expiración del token que es un min
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Parámetros de nuestro token: el usuario, fecha de expiración
    access_token = {"sub": user.username, "exp": expire}
    # Para generar el token le pasamos la información a cifrar que es el usuario en sí y la fecha de expiración
    # También le pasamos la semilla y el algoritmo utilizado para generar el token
    token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
    # Si todo va bien, devolvemos el token generado
    return {"access_token": token, "token_type": "bearer"}