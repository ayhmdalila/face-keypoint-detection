import streamlit as st
import tempfile
import os
from face_mesh_processor import process_video, get_video_codec, transcode_to_h264, finalize_video_encoding
import io

st.title("🎯 Face Keypoint Detection")
st.write("Upload a video and see facial landmarks applied using MediaPipe.")

uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_input:
        temp_input.write(uploaded_file.read())
        input_path = temp_input.name
    # After saving uploaded file
    codec = get_video_codec(input_path)
    if codec == "av1":
        st.warning("AV1 codec detected. Transcoding to H.264 for compatibility...")
        input_path = transcode_to_h264(input_path)

    st.info("Processing video... This may take a moment.")
    output_path = process_video(input_path)
    output_path = finalize_video_encoding(output_path)

    st.success("Done! Here's the processed video:")

    with open(output_path, "rb") as f:
        video_bytes = f.read()

    st.video(io.BytesIO(video_bytes), format="video/mp4")

    st.download_button("Download Processed Video", data=open(output_path, "rb").read(), file_name="face_keypoints.mp4")