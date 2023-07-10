import os
import glob
from elevenlabs import save, generate, set_api_key, voices

set_api_key("<YOUR_API_KEY_HERE>")  # replace with your actual API key

voice = "Your_Voice_id"  # Set your preferred voice
model = "elevenlabs_monolingual_v1" #set your preferred model

input_folder = "path/to/input/folder"  # Enter the path to your folder
output_folder = "path/to/output/folder"  # Enter the path to output folder



def text_to_speech(file_path, output_folder, voice):
    with open(file_path, 'r') as file:
        text = file.read()

    audio = generate(text=text, voice=voice)

    output_path = os.path.join(output_folder, os.path.basename(file_path).replace('.txt', '.mp3'))
    with open(output_path, "wb") as output:
        output.write(audio)

    return output_path

def main():

    os.makedirs(output_folder, exist_ok=True)

    txt_files = glob.glob(os.path.join(input_folder, '*.txt'))

    for txt_file in txt_files:
        text_to_speech(txt_file, output_folder, voice)

if __name__ == "__main__":
    main()