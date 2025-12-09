
from datetime import datetime, timezone, timedelta
from fastapi import APIRouter, Depends, HTTPException
#Importar JWT
import jwt
#Trabajar las excepciones de los tokens
from jwt.exceptions import InvalidTokenError
#Libreria para aplicar un hash a la contraseña
from pwdlib import PasswordHash
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2 = OAuth2PasswordBearer(tokenUrl = "login")

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
    "password" : "$argon2id$v=19$m=65536,t=3,p=4$xWJA1VO51NuvrtX3i1YpIA$QTj+B6izE18706s49jgUtc N5ezJh5vQ9g d7udvtc Y/k"
    }


}

@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username not in users_db:
        # 1. Hashear la contraseña
        hashed_password = password_hash.hash(user.password)
        # 2. Reemplazar la contraseña plana con la hasheada
        user.password = hashed_password
        # 3. Guardar el nuevo usuario en la "base de datos"
        users_db[user.username] = user.model_dump()
        # 4. Devolver el objeto de usuario (ahora con la contraseña hasheada)
        return user
    
    # Si el usuario ya existe
    raise HTTPException(status_code=409, detail="User already exists")
    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    print(user_db)

    if not user_db:
        # Si el usuario NO existe, lanzamos el error genérico
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    
    # Si el usuario existe en la base de datos 
    # Comprobamos las contraseñas
    # Creamos el usuario de tipo UserDB 
    user = UserDB(**users_db[form.username])

    try:
        if password_hash.verify(form.password, user.password):
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = {"sub": user.username, "exp": expire}
            
            # Generamos el token
            token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
            return {"access_token": token, "token_type": "bearer"}

        #raise HTTPException(status_code=401, detail="Contraseña incorrecta") 
    except:
        raise HTTPException(status_code=400, detail="Error en la autenticación")
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

async def authentication(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM).get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Credenciales de autenticacion inválidas",
                                headers={"WWW-Authenticate": "Bearer"})
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Credenciales de autenticacion inválidas",
                                headers={"WWW-Authenticate": "Bearer"})
    
    user = User(**users_db[username])
