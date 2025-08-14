FROM python:3.12.11

WORKDIR /app_eora_assistant

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]