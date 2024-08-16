import pandas as pd 

story = ''
word_count = []
prompts = []
print("Enter Bgm prompt: ")
bgm_prompt = input()
print("Enter voice gender: ")
voice_type = input()

def input():
    global story, word_count, prompts
    script = pd.read_csv('.\\Input\input.csv')
    for line in script['voiceover']:
        story += line
        story += ' '
        word_count.append(len(line.split()))
    
    for prompt in script['image']:
        prompts.append(prompt)
    
    
