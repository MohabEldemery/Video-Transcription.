from pathlib import Path
import whisper
from whisper.utils import get_writer
import warnings
warnings.filterwarnings("ignore", message=".*FP16 is not supported on CPU.*")

# Load Whisper model
model = whisper.load_model("base")   # you can also try "small", "medium", or "large"

# Input video and output folder & Run transcription
video_path = r"D:\whisper\review.mp4"
output_dir = r"D:\whisper"

result = model.transcribe(video_path)
print("Transcript:\n", result["text"])

# Save SRT file
srt_writer = get_writer("srt", str(output_dir))
srt_writer(result, video_path)

print("Saved SRT in", output_dir)
