FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    wget \
    bash \
    ffmpeg \
    neofetch \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Install python deps
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel \
    && pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000

CMD ["python3", "-m", "devgagan"]
