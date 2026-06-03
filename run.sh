#!/bin/bash

# Quick Start Script for Employee Management System

echo ""
echo "========================================"
echo "Employee Management System - Quick Start"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

echo "Checking Python installation..."
python3 --version

echo ""
echo "Installing dependencies..."
cd backend
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo ""
echo "Dependencies installed successfully!"
echo ""
echo "Starting Flask server..."
echo ""
echo "========================================"
echo "Server running on http://localhost:5000"
echo "Open this URL in your web browser"
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

python3 app.py
