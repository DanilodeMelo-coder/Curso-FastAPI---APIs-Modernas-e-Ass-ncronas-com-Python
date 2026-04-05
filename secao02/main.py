from fastapi import FastAPI

#  & "C:\Users\Danilo\Envs\famp-secao02\Scripts\Activate.ps1"

app = FastAPI()

@app.get("/")
async def raiz():
    return{"menssage": "Curso FastAPi"}