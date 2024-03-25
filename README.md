# projeto simples com docker e Vue.js

Para rodar, execute:
cd frontend
docker build -t frontend -f docker/Dockerfile .
docker run -v ${PWD}/src:/app/src -p 9000:8080 frontend