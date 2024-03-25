# projeto simples com docker e Vue.js

Para rodar, execute:
cd frontend
docker build -t frontend -f docker/Dockerfile .
docker run -p 9000:8080 frontend