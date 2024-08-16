import Input
import Text_to_image
import Text_to_speech
import Text_to_bgm
import Speech_to_word_timestamps
import Slideshow
import merge_audio_video

if __name__ == '__main__':
    Input.input()
    Text_to_image.text_to_image_local(Input.prompts)
    Text_to_speech.text_to_speech(Input.story, Input.voice_type)
    Text_to_bgm.text_to_bgm(Input.bgm_prompt)
    Speech_to_word_timestamps.speech_to_word_timestamps()
    Slideshow.create_slideshow(Speech_to_word_timestamps.end, Speech_to_word_timestamps.word, Input.word_count, Text_to_image.image_paths)
    merge_audio_video.create_final_result()