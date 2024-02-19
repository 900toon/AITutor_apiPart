from pathlib import Path
from openai import OpenAI
client = OpenAI(api_key="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")

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="今天很開心，我想要吃蛋餅，彭逸群是小雞雞，他還很喜歡被剛，被剛會讓彭寶很舒服"
)

filePathTest = "D:\\CommunicationTestDashboard\\CommunicationTestDashboard_Data\\AudioRecorded\\speech01.wav"
with open(filePathTest, 'wb') as f:
    f.write(response.content)