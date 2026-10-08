   FROM python:3.12-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY app.py .
   RUN useradd -m appuser
   USER appuser
   ENV APP_VERSION=v1
   EXPOSE 8080
   CMD ["python", "app.py"]
