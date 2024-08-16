import requests
import os
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv

def text_to_bgm(bgm_prompt):
	print("Generating bgm from text.....")
	load_dotenv()
	access_token = os.getenv('access_token')

	headers = {"Authorization": f"Bearer {access_token}"}

	API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"

	def query(payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.content

	audio_bytes = query({
		"inputs": bgm_prompt
	})

	output_path = './Output/bgm.mp3'
	os.makedirs(os.path.dirname(output_path), exist_ok=True)

	audio = AudioSegment.from_file(BytesIO(audio_bytes), format='flac')
	audio.export(output_path, format='mp3')

	audio = AudioSegment.from_file(output_path)
	loop_audio = audio+audio+audio
	loop_audio.export(output_path, format='mp3')
	print("Bgm generated!")
