from openai import OpenAI
client = OpenAI(api_key="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")

filePath = "D:\\CommunicationTestDashboard\\CommunicationTestDashboard_Data\\AudioRecorded\\temp0.wav"
audio_file = open(filePath, "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)
print(transcript)