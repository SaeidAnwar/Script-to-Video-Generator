# How to generate video
## 1. Install req libraries
1. dotenv
2. requests
4. pydub
5. torch
6. diffusers
7. safetensors
8. meta_ai_api
9. gradio_client
10. pandas
11. cv2
12. vosk

## 2. Required API keys
1. Hugging face acces_token
2. Eleven labs api_key

## 3. Install ffmpeg
Link for the steps: https://www.editframe.com/guides/how-to-install-and-start-using-ffmpeg-in-under-10-minutes

## 4. Input
Create a csv file with "voiceover" and "image" column. "voiceover" contains the line of story and "image" contains the prompt for the image to use with that line of story.

## 5. Folders
Create these folders with same name:
1. Img
2. Output
3. models

## 6. Model
Download a speech to text model from vosk and put unzipped folder in the models folder and use the path for model_path in Speech_to_word_timestamps.py file.

## 7. Run 
Run the main.py and give the bgm prompt and voiceover gender and wait, output will be a result.mp4 file.



