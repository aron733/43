.PHONY: help install dev build test clean deploy

help:
	@echo "Trading Platform 43 - Make Commands"
	@echo "====================================="
	@echo "make install    - Install dependencies"
	@echo "make dev        - Run development environment"
	@echo "make build      - Build for production"
	@echo "make test       - Run tests"
	@echo "make clean      - Clean up"
	@echo "make docker     - Run with Docker Compose"

install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

dev:
	@echo "Starting development servers..."
	@echo "Backend on http://localhost:5000"
	@echo "Frontend on http://localhost:3000"
	@concurrently "cd backend && python main.py" "cd frontend && npm start"

build:
	cd frontend && npm run build

test:
	cd backend && python -m pytest
	cd frontend && npm test

clean:
	rm -rf frontend/build
	rm -rf backend/__pycache__
	find . -type d -name __pycache__ -exec rm -rf {} +

docker:
	docker-compose up -d

docker-prod:
	docker-compose -f docker-compose.prod.yml up -d