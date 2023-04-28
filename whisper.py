import whisper

model = whisper.load_model("base")
result = model.transcribe("./audio_sample.wav")
print(result["text"])
with open("audio_sample.txt", "w+") as f:
    f.write(result["text"])