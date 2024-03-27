FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /uploads && \
    chown -R root:root /uploads && \
    chmod -R 755 /uploads

COPY . .

EXPOSE 5000

CMD ["python", "src/app.py"]