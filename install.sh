# Python environment
python -m venv .venv
source .venv/bin/activate

# Package install
pip install -r requirements.txt
pip install -e .

# Data building
mathnets --download
mathnets --build