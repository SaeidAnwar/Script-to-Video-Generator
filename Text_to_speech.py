import json
import random
import requests
import os
from dotenv import load_dotenv

def text_to_speech(story, voice_type):
    print("Generating speech from text.....")
    load_dotenv()
    x_api_key = os.getenv('xi_api_keya')

    with open('voices.json', 'r') as f:
        voice_data = json.load(f)

    male_voice_ids = []
    female_voice_ids = []
    for voice in voice_data['voices']:
        if voice['labels']['use_case'] == 'narration':
            if voice['labels']['gender'] == 'male':
                male_voice_ids.append(voice['voice_id'])
            else:
                female_voice_ids.append(voice['voice_id'])

    voice_id = ''
    if voice_type == 'male':
        voice_id = random.choice(male_voice_ids)
    else:
        voice_id = random.choice(female_voice_ids)


    CHUNK_SIZE = 1024
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": f"{x_api_key}"
    }

    data = {
        "text": story,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    output_path = './Output/voiceover.mp3'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.post(url, json=data, headers=headers)
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    print("Speech generated!")