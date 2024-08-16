import wave
import json
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer, SetLogLevel

word = []
end = []

def speech_to_word_timestamps():
    print("Generating timestamps for each words.....")
    global word, end
    model_path = "./models/vosk-model-en-us-0.22"
    audio_filepath = "./Output/voiceover.mp3"
    sound = AudioSegment.from_mp3(audio_filepath)
    audio_filename = "./Output/audio.wav"
    sound.export("./Output/audio.wav", format="wav")

    model = Model(model_path)
    wf = wave.open(audio_filename, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)   

    part_result = json.loads(rec.FinalResult())
    results.append(part_result)
   
    for res in results:
        for i in res['result']:
            end.append(i['end'])
            word.append(i['word'])
    print("Timestamps generated!")
