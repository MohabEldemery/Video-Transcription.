from pathlib import Path
import whisper
from whisper.utils import get_writer
import warnings
warnings.filterwarnings("ignore", message=".*FP16 is not supported on CPU.*")

# Load Whisper model.
model = whisper.load_model("base")   # you can also try "small", "medium" Or or "large" Or "turbo" but RAM Usage & Processing time will inc.

# Input video and output folder & Run transcription
video_path = r"D:\whisper\review.mp4"
output_dir = r"D:\whisper"

result = model.transcribe(video_path)
print("Transcript:\n", result["text"])

# Save SRT file
srt_writer = get_writer("srt", str(output_dir))
srt_writer(result, video_path)

print("Saved SRT in", output_dir)
#
# # 3. Setup summarizer
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#
# # --- Helper: chunk text ---
# def chunk_text(text, max_words=400):
#     words = text.split()
#     for i in range(0, len(words), max_words):
#         yield " ".join(words[i:i+max_words])
#
# # 4. Summarize in chunks
# summaries = []
# for chunk in chunk_text(full_text, max_words=400):
#     try:
#         s = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
#         summaries.append(s)
#     except Exception as e:
#         print("Error summarizing chunk:", e)
#
# # Combine partial summaries into final summary
# final_summary = " ".join(summaries)
#
# print("\nSummarized Transcript:\n", final_summary)
#
# # 5. Save summary to TXT
# summary_path = Path(output_dir) / "summary.txt"
# with open(summary_path, "w", encoding="utf-8") as f:
#     f.write(final_summary)
#
# print("Saved Summary TXT in", summary_path)





