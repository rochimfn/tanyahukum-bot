FROM python:3.7-slim

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

ENTRYPOINT ["python", "main.py"]
CMD ["vps"]