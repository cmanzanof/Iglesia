from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Configura CORS para permitir el frontend de Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://p-gina-de-la-iglesia-gray-grass.reflex.run/"],  # Cambia esto por tu dominio de Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI en Railway!", "mensaje2": "¡Ya entendimos!"}

@app.get("/pruebas")
def read_roo():
    return {"pruebas": "¡prueba funcional!"}
