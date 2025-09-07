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
    echo "⚠️ Recuerda editar .env con tus credenciales reales de MySQL"
fi

echo "✅ Configuración lista. Para correr la API:"
echo "   source venv/bin/activate && python src/app.py"
