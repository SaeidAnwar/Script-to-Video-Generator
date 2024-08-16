import subprocess
import os

def merge_audio_with_video(audio_path, video_path, output_path):
    command = f'ffmpeg -y -i {video_path} -i {audio_path} -filter_complex "[0:a][1:a]amerge=inputs=2[a]" -map 0:v -map "[a]" -c:v copy -ac 2 -shortest {output_path}'
    print(command)
    subprocess.run(command)

def add_audio_to_video(audio_path, video_path, output_path):
    command = f'ffmpeg -y -i {video_path}  -i {audio_path} -map 0 -map 1:a -c:v copy -shortest {output_path}'
    subprocess.run(command)

def avi_to_mp4(video_path, output_path):
    command = f"ffmpeg -y -i {video_path} -c:v copy -c:a copy {output_path}"
    subprocess.run(command)

def create_final_result():
    print("Creating final result.....")
    output_path = "./Output/output.mp4"
    audio_path = "./Output/voiceover.mp3"
    bgm_path = "./Output/bgm.mp3"
    video_path = "./Output/output.avi"
    result_path = "result.mp4"

    add_audio_to_video(audio_path, video_path, output_path)
    merge_audio_with_video(bgm_path, output_path, result_path)
    print("Final result created!!! 0_0")
