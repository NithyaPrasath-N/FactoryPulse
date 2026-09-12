# ============================================
# FactoryPulse - Simulator Service Dockerfile
# ============================================

# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Default command
CMD ["python", "-m", "src.replayer"]
