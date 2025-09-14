# 🧠 Face Keypoint Detection with MediaPipe & OpenCV

This project uses [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/) to detect and visualize facial landmarks in video frames. It leverages MediaPipe's FaceMesh model to track keypoints and overlays them on the input video.



## 📦 Features

- Real-time face mesh detection on video input
- Visual overlay of facial landmarks using OpenCV
- Dockerized setup for easy deployment
- Qt-based GUI rendering inside container (with X11 support)



## 🚀 Getting Started

### 🔧 Prerequisites

- Docker installed on your system
- X11 server running (for GUI display)
  - On Linux: native X11
  - On Windows (WSL): use [VcXsrv](https://sourceforge.net/projects/vcxsrv/) or [X410](https://x410.dev/)
  - On macOS: use [XQuartz](https://www.xquartz.org/)



## 🐳 Run with Docker

### 1. Build the Docker image

(Note: Extra GUI steps are not needed if you are running this on windows locally, but this was developed in WSL.)

```bash
docker build -t face-keypoint-tracking .

2. Allow Docker to access your display
On Linux:
xhost +local:docker


On WSL (Windows Subsystem for Linux):
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
xhost +local:docker

3. Run the container
docker run -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           --net=host \
           face-keypoint-tracking

```

## 📂 Project Structure

```
face-keypoint-detection/
├── Dockerfile
├── requirements.txt
├── main.py
└── muhammad_ali.mkv  # Replace with your own video file
```



## 🧪 Usage

Once the container starts, it will:
- Load the video file muhammad_ali.mkv
- Detect facial landmarks frame-by-frame
- Display the annotated video in a GUI window
Press q to quit the video playback.



## 🛠 Troubleshooting

Qt plugin error: Could not connect to display
Make sure:
- Your X11 server is running
- DISPLAY is correctly set
- You’ve run xhost +local:docker
Plugin not loading: xcb not found
Ensure the following packages are installed in the container:
libxcb1 libx11-xcb1 libxcb-glx0 libxcb-xinerama0 libxcb-render0 libxcb-shape0 libxcb-shm0 libxrender1 libxext6 libxkbcommon-x11-0 libxcb-cursor0



## 📜 License

This project is open-source.



## 🙌 Acknowledgments

- MediaPipe
- OpenCV



