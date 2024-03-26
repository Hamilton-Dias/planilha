# projeto simples com docker e Vue.js

Para rodar o frontend, execute:
<pre>
cd frontend
docker build -t frontend -f docker/Dockerfile .
docker run -v ${PWD}/src:/app/src -p 9001:8080 frontend
</pre>
<br>
Para rodar o backend, execute:
<pre>
cd backend
docker build -t backend -f docker/Dockerfile .
docker run -v ${PWD}/src:/app/src -p 9002:5000 backend
</pre>
Acesse http://localhost:9001 e http://localhost:9002 para acessar o frontend e o backend, respectivamente