if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ -d "tests" ]; then
  pytest tests
else
  echo "No tests directory found."
fi

python main.py
