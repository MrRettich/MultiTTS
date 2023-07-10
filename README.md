# # Text-to-Speech Conversion using ElevenLabs API

This script allows you to convert text files to speech using the ElevenLabs API. It reads text files from a specified input folder, generates speech using the API, and saves the resulting audio files in an output folder.

## Requirements

- Python 3.x
- ElevenLabs API key (sign up at [ElevenLabs website](https://beta.elevenlabs.io//))

## Installation

1. Clone or download the script to your local machine.
2. Install the required Python packages by running the following command:

   ```shell
   pip install elevenlabs
   ```

## Configuration

Before running the script, you need to set up the following variables in the script:

- `set_api_key("<YOUR_API_KEY_HERE>")`: Replace `<YOUR_API_KEY_HERE>` with your actual ElevenLabs API key.
- `voice = "Your_Voice_id"`: Set `Your_Voice_id` to your preferred voice ID. You can find the available voice IDs in the ElevenLabs API documentation.
- `model = "elevenlabs_monolingual_v1"`: Set `elevenlabs_monolingual_v1` to your preferred model. You can find the available models in the ElevenLabs API documentation.
- `input_folder = "path/to/input/folder"`: Set `path/to/input/folder` to the path of the folder containing your input text files.
- `output_folder = "path/to/output/folder"`: Set `path/to/output/folder` to the path where you want to save the output audio files.

## Usage

1. Place your text files in the input folder specified in the script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the following command to execute the script:

   ```shell
   python app.py
   ```

   
4. The script will convert each text file in the input folder to speech using the ElevenLabs API and save the resulting audio files in the output folder.
5. Once the script has finished processing all the files, you will find the converted audio files in the output folder.

## Note

- Ensure that you have a stable internet connection while running the script, as it requires access to the ElevenLabs API.
- Make sure that the input and output folders exist before running the script. The script will not create the folders automatically.
- The script uses the `.txt` extension to identify the input text files. Only files with the `.txt` extension will be processed.

## License

This project is licensed under the terms of the MIT license.