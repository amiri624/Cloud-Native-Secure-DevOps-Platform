.PHONY: install test run docker-build docker-run

install:
 pip install -r requirements.txt

test:
 pytest -q

run:
 uvicorn main:app --host 0.0.0.0 --port 8000 --reload

docker-build:
 docker build -t devsecops-app .

docker-run:
 docker run -p 8000:8000 devsecops-app
