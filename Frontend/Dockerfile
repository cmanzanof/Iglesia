# Frontend/Dockerfile
FROM python:3.12-slim

# Instala unzip que Reflex necesita
RUN apt-get update && apt-get install -y unzip curl git && rm -rf /var/lib/apt/lists/*

# Crea el entorno de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .

# Instala dependencias del frontend
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto del frontend
EXPOSE 3000

# Comando para iniciar Reflex
CMD ["reflex", "run", "--env", "prod"]
