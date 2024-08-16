from gradio_client import Client
import os
import shutil
import torch
import requests
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel, EulerDiscreteScheduler, DiffusionPipeline
from safetensors.torch import load_file
from meta_ai_api import MetaAI
import multiprocess
import threading

image_paths = []
def text_to_image_local(prompts):
        global image_paths
        # Load model.
        # base = "stabilityai/stable-diffusion-xl-base-1.0"
        # unet = UNet2DConditionModel.from_config(base, subfolder="unet").to("cpu", torch.float32)
        # unet.load_state_dict(load_file("./models/sdxl_lightning_8step_unet.safetensors", device="cpu"))

        # Ensure sampler uses "trailing" timesteps.
        # pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")

        pipeline = DiffusionPipeline.from_pretrained("Yntec/epiCPhotoGasm")
        pipeline.to("cpu")

        def gen_image(prompt, idx):
                pipeline(prompt, num_inference_steps=10, width=512, height=512).images[0].save("./Img/" + str(idx) + '.png')
                return
        
        threads = []
        i = 0
        for prom in prompts:
                # t = threading.Thread(target = gen_image, args=(prom, i))
                # threads.append(t)
                # t.start()
                pipeline(prom, num_inference_steps=20, width=512, height=512).images[0].save("./Img/" + str(i) + '.png')
                image_paths.append("./Img/" + str(i) + '.png')
                print("image " + str(i) + " generated!")
                i += 1
 
        # for t in threads:
        #         t.join()

def text_to_image_meta(prompts):
        ai = MetaAI(fb_email="8920913799", fb_password="saeid9013")
        global image_paths
        print("Gerating images.....")
        i = 0
        for prom in prompts:
                response = ai.prompt(message="/imagine " + prom)
                
                image_url = response["media"][0]["url"]

                res = requests.get(image_url, stream=True)

                if res.status_code == 200:
                        with open("./Img/" + str(i) + '.jpeg', 'wb') as f:
                                shutil.copyfileobj(res.raw, f)
                                image_paths.append("./Img/" + str(i) + '.jpeg')
                        print('Image sucessfully Downloaded: ', "./Img/" + str(i) + '.jpeg')
                else:
                        print('Image Couldn\'t be retrieved')
                i += 1

def text_to_image(prompts):
        global image_paths
        client = Client("stabilityai/stable-diffusion-3-medium")
        i = 0
        for prompt in prompts:
                print("generating image " + str(i) + ".....")
                result = client.predict(
                        prompt=prompt,
                        negative_prompt="low quality, aritfacts, distortion",
                        seed=0,
                        randomize_seed=True,
                        width=1024,
                        height=1024,
                        guidance_scale=5,
                        num_inference_steps=28,
                        api_name="/infer"
                )
                output_path = './Img/'
                shutil.move(result[0], output_path + '/'+ str(i) + '.webp')
                image_paths.append(output_path + str(i) + ".webp")
                print("image " + str(i) + " generated!")
                i += 1





    