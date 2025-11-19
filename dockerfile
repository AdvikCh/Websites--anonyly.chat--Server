FROM python:3.11-slim
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY "Source code-Server.py" .
EXPOSE 10000
CMD ["python", Source code-Server.py"]
