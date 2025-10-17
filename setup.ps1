# Setup script for EventLync

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install backend dependencies
pip install -r backend/requirements.txt

# Set environment variables
$env:FLASK_APP = "backend.run"
$env:FLASK_ENV = "development"

# Initialize and upgrade database
cd backend
flask db upgrade

Write-Host "Setup complete! Run 'flask run' to start the development server."
