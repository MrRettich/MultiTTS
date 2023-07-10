# Checks which voices are available for you and pritnts it into the console.

from elevenlabs import set_api_key, Voices

set_api_key("<YOUR_API_KEY_HERE>")  # replace with your actual API key

voices = Voices.from_api()
print(voices[0])
print(voices)