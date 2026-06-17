.PHONY: install run lint format test clean

install:
	@echo "Setting up virtual environment and installing dependencies..."
	python -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

run:
	@echo "Running the application..."
	streamlit run app.py

clean:
	@echo "Cleaning up __pycache__ directories and .pyc files..."
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete