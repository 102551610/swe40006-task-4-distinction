# --- Stage 1: Build & Dependencies ---
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Stage 2: Final Runtime Environment ---
FROM python:3.11-slim AS runner
WORKDIR /app

# Copy dependencies and application logic
COPY --from=builder /install /usr/local
COPY main.py .

# COPY SSL CERTIFICATES FOR LOCAL HTTPS
COPY cert.pem key.pem ./

EXPOSE 8000

# Execute Uvicorn natively with SSL configuration enabled
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "key.pem", "--ssl-certfile", "cert.pem"]
