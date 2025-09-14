FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

ENV QT_DEBUG_PLUGINS=1
# Install dependencies first to leverage caching
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    libxcb1 \
    libx11-xcb1 \
    libxcb-glx0 \
    libxcb-xinerama0 \
    libxcb-render0 \
    libxcb-shape0 \
    libxcb-shm0 \
    libxrender1 \
    libxext6 \
    libxkbcommon-x11-0
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install libxcb-cursor0 -y
RUN pip install -r requirements.txt --no-cache-dir --default-timeout=300000 --retries=300

# Copy the rest of the application files
COPY . .

# Command to run the application
CMD ["python", "main.py"]