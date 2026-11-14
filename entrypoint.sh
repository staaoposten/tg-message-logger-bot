#!/bin/sh
set -e

cat > /app/config.ini <<EOF
[BOT]
token = ${BOT_TOKEN}
allowed_ids = ${ALLOWED_IDS}

[DATABASE]
username = ${DB_USER}
password = ${DB_PASSWORD}
ip = ${DB_HOST:-db}
port = ${DB_PORT:-3306}
db = ${DB_NAME}
EOF

exec python main.py
