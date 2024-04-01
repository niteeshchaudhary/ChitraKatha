from transformers import pipeline, set_seed,AutoTokenizer,AutoConfig,AutoModelForCausalLM
# import intel_extension_for_pytorch as ipex

import torch
from diffusers import StableDiffusionPipeline

from gtts import gTTS
from moviepy.editor import  AudioFileClip

from moviepy.editor import ImageClip
from moviepy.editor import AudioFileClip
from moviepy.editor import ColorClip,CompositeVideoClip,concatenate_videoclips

pipe = pipeline("text-generation", model="openai-community/gpt2")

set_seed(122)

text_ = ""
story=""
set_seed(200)
duration=0
audio= None

def generate_story(text):
    global pipe,story,text_
    # Set the maximum number of tokens
    max_length = 100
    text_=text
    prompt = "continue the story" + text_

    # Generate the story
    story = pipe(
        prompt,
        max_length=max_length,
        truncation=True
    )[0]['generated_text'][len(prompt)+2:]
    story=text_+story
    return story

def generate_audio():
    global duration,audio,story
    narration_text = story
    narration = gTTS(text=narration_text, lang='en', slow=True, tld='com')
    narration.save("narration.mp3")
    audio = AudioFileClip("narration.mp3")
    duration = audio.duration

def generate_images():
    global pipe, num_images, duration, story
    pipe = StableDiffusionPipeline.from_pretrained("digiplay/majicMIX_realistic_v6", torch_dtype=torch.float32)  # Change torch_dtype to float32
    pipe = pipe.to("cuda")
    pipe.safety_checker = None

    h = 800  # height of the image
    w = 640  # width of the image
    steps = 2  # number of updates the system makes before giving the result, making it more accurate
    guidance = 10  # how closely you want the image to be related to the prompt that you have typed
    neg = "easynegative,no repetation, lowres,partial view, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot,"

    num_images = int(duration/10)
    size = len(story)//num_images
    for i in range(num_images):
        prompt = story[i*size:(i+1)*size]
        image = pipe(prompt, height=h, width=w, number_inference_steps=steps, guidance_scale=guidance, negative_prompt=neg).images[0]
        image.save(f"./image_created/image_{i+1}.png")  # Save the image with a unique name

def generator_video():
    # Create a blank video clip with the same duration as the audio
    global duration, story, audio, num_images
    video = ColorClip((1280, 720), color=(0, 0, 0), duration=duration)

    # Set the text for the video
    txt = story

    # Add the text clip to the video
    video = video.set_audio(audio)
    video = video.set_duration(duration)
    video = video.set_fps(24)
    video = video.set_audio(audio)
    video = video.set_duration(duration)
    video = video.set_fps(24)
    video = CompositeVideoClip([video])

    # Add images to the video
    image_clips = [ImageClip(f"./image_created/image_{i}.png").set_duration(duration/num_images) for i in range(1, num_images+1)]

    # Create a video from the images
    images_video = concatenate_videoclips(image_clips, method="compose")

    # Overlay the images video on top of the main video
    final_video = CompositeVideoClip([video.set_position(('center', 'center')), images_video.set_position(('center', 'center'))])

    # Write the final video to a file
    final_video.write_videofile("story_video.mp4", codec='libx264', fps=24)