REM Python enviroment
python -m venv .venv
.\.venv\bin\Activate.ps1

REM Package install
pip install -r requirements.txt
pip install -e .

REM Data building
mathnets --download
mathnets --build