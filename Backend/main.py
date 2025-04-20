from fastapi import FastAPI

app = FastAPI()
# Configura CORS para permitir el frontend de Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://front-iglesia.vercel.app"],  # Cambia esto por tu dominio de Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI en Railway!"}
