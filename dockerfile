FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY api_client.py .
CMD ["python", "api_client.py"]