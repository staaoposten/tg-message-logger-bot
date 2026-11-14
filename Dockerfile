FROM python:3.12-slim
RUN apt update;apt install -y git;rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pybabel compile -d locales -D messages
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
