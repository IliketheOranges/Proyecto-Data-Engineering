FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV STRESS_SECONDS=10
ENV STRESS_INTENSITY=10000000

EXPOSE 5000

CMD ["python", "app/app.py"]
