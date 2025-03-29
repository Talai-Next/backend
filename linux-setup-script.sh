#!/bin/bash

# ===== Get the directory this script is in =====
BASEDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$BASEDIR"
echo "====================================================="
echo "Script started at: $BASEDIR"
echo "====================================================="

# ===== Ask for environment values =====
echo
echo "===== Configure Environment Variables ====="
read -p "Enter DATABASE_URL: " DATABASE_URL
read -p "Enter DJANGO_SECRET_KEY: " DJANGO_SECRET_KEY

# ===== Repo URLs =====
API_REPO="https://github.com/Talai-Next/talai-api"
BACKEND_REPO="https://github.com/Talai-Next/backend"
FRONTEND_REPO="https://github.com/Talai-Next/frontend"

# ===== Branches =====
API_BRANCH="master"
BACKEND_BRANCH="predict_service"
FRONTEND_BRANCH="demo"

# ===== Directory Names =====
API_DIR="talai-api"
BACKEND_DIR="backend"
FRONTEND_DIR="frontend"

# ===== Clone Repositories =====
echo
echo "Cloning repositories with their respective branches..."

if [ ! -d "$API_DIR" ]; then
    echo "Cloning talai-api from branch $API_BRANCH..."
    git clone -b "$API_BRANCH" "$API_REPO" "$API_DIR"
else
    echo "talai-api already exists. Skipping clone."
fi

if [ ! -d "$BACKEND_DIR" ]; then
    echo "Cloning backend from branch $BACKEND_BRANCH..."
    git clone -b "$BACKEND_BRANCH" "$BACKEND_REPO" "$BACKEND_DIR"
else
    echo "backend already exists. Skipping clone."
fi

if [ ! -d "$FRONTEND_DIR" ]; then
    echo "Cloning frontend from branch $FRONTEND_BRANCH..."
    git clone -b "$FRONTEND_BRANCH" "$FRONTEND_REPO" "$FRONTEND_DIR"
else
    echo "frontend already exists. Skipping clone."
fi

# ===== Detect Python =====
echo
echo "Detecting Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    echo "Python found: $PYTHON_CMD"
else
    echo "Python3 not found. Please install it."
    exit 1
fi

# ===== talai-api Setup =====
echo
echo "===== talai-api Setup ====="
cd "$BASEDIR/$API_DIR"

echo "Creating virtual environment..."
$PYTHON_CMD -m venv venv

echo "Activating environment and installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo "Creating .env file for talai-api..."
cat <<EOF > .env
DATABASE_URL=$DATABASE_URL
DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
EOF

echo "Running database migrations..."
$PYTHON_CMD manage.py migrate

echo "Starting talai-api server on port 8080..."
gnome-terminal -- bash -c "source venv/bin/activate && $PYTHON_CMD manage.py runserver 8080; exec bash"

deactivate
cd "$BASEDIR"

# ===== backend Setup =====
echo
echo "===== backend Setup ====="
cd "$BASEDIR/$BACKEND_DIR"

echo "Creating virtual environment..."
$PYTHON_CMD -m venv venv

echo "Activating environment and installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo "Creating .env file for backend..."
cat <<EOF > .env
DATABASE_URL=$DATABASE_URL
DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
EOF

echo "Running database migrations..."
$PYTHON_CMD manage.py migrate

echo "Starting backend server on port 8000..."
gnome-terminal -- bash -c "source venv/bin/activate && $PYTHON_CMD manage.py runserver 8000; exec bash"

deactivate
cd "$BASEDIR"

# ===== frontend Setup =====
echo
echo "===== frontend Setup ====="
cd "$BASEDIR/$FRONTEND_DIR"

echo "Installing frontend dependencies..."
npm install

echo "Starting frontend server..."
gnome-terminal -- bash -c "npm run dev; exec bash"

cd "$BASEDIR"

echo
echo "====================================================="
echo "All servers are now running."
echo "-----------------------------------------------------"
echo "talai-api : http://localhost:8080"
echo "backend   : http://localhost:8000"
echo "frontend  : http://localhost:5173"
echo "====================================================="
