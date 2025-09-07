#!/bin/bash

echo "🚀 Iniciando configuración del entorno..."

# Crear venv si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar venv
source venv/bin/activate

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Crear archivo .env si no existe
if [ ! -f ".env" ]; then
    echo "⚙️ Creando archivo .env desde .env.example..."
    cp .env.example .env
    echo "⚠️ Recuerda editar .env con tus credenciales reales de MySQL si es necesario"
fi

# Verificar si el contenedor MySQL ya existe
if [ ! "$(docker ps -aq -f name=mysql-futbol)" ]; then
    echo "🐬 Creando contenedor MySQL..."
    docker run -d \
        --name mysql-futbol \
        -e MYSQL_ROOT_PASSWORD=rootpass \
        -e MYSQL_DATABASE=futbol \
        -p 3307:3306 \
        mysql:8.0
else
    echo "🐬 Contenedor MySQL ya existe, iniciando..."
    docker start mysql-futbol
fi

echo "✅ Configuración lista. Para correr la API:"
echo "   source venv/bin/activate && python src/app.py"
