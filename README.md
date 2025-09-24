# Video Transcription and SRT Generator

This project uses OpenAI Whisper, a powerful speech recognition model, to convert video files into text and create .srt subtitle files. It works on both CPU and GPU, automatically handling FP16 warnings on CPU, and uses PyTorch for running the model and FFmpeg for processing audio and video. There is also an optional feature to summarize transcripts using Hugging Face Transformers (facebook/bart-large-cnn), which can create shorter, easy-to-read versions of the text. The tool is easy to install, requires few dependencies, and is designed to help users quickly turn spoken content from videos into readable text, subtitles, or summaries, making video transcription and subtitle generation simple and efficient.

---

## Features

- Transcribe video files (e.g., `.mp4`) to text.
- Generate SRT subtitles from the transcription.
- Optional summarization of transcript (commented in code).
- CPU/GPU compatible.
- Supports multiple Whisper models (tiny, base, small, medium, large) depending on accuracy and speed needs:
- Whisper Model Options:
    tiny – Fastest, lower accuracy
    base – Balanced speed and accuracy
    small – Higher accuracy
    medium – Very accurate
    large – Highest accuracy, slower and requires more resources

- Install required packages:

pip install --upgrade pip setuptools wheel
pip install openai-whisper ffmpeg-python
pip install torch      
