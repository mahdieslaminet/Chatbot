چت‌بات با ویژگی‌های پیشرفته

این پروژه یک چت‌بات پیشرفته است که از تکنولوژی‌های مدرن برای ایجاد تعاملات پویا و کارآمد بهره می‌برد. اجزای اصلی این چت‌بات عبارتند از:

اجزای اصلی

1. TTS (تبدیل متن به گفتار)
متن‌های تولید شده توسط چت‌بات را به گفتاری طبیعی تبدیل می‌کند تا امکان خروجی صوتی برای کاربران فراهم شود.


2. STT (تبدیل گفتار به متن)
گفتار ورودی کاربران را به متن تبدیل می‌کند تا توسط چت‌بات پردازش شود و تعامل صوتی امکان‌پذیر باشد.


3. LANGDETECT (تشخیص زبان)
زبان ورودی کاربر را به صورت خودکار تشخیص می‌دهد تا پردازش و پاسخ‌دهی به زبان مناسب انجام شود.


4. تشخیص زبان متن
زبان متن ورودی را شناسایی می‌کند و امکان پشتیبانی از چندین زبان را برای کاربران فراهم می‌نماید.


5. ANONYMOUS SOUND (صوت ناشناس)
از تکنیک‌های ناشناس‌سازی صدا برای حفظ حریم خصوصی و امنیت کاربران در ارتباطات صوتی استفاده می‌کند.


6. Voice Conversion (تبدیل صدا)
صدای یک فرد را به صدای دیگری تبدیل می‌کند در حالی که محتوای گفتار اصلی حفظ می‌شود، و امکان شخصی‌سازی پاسخ‌های صوتی را فراهم می‌سازد.



ویژگی‌های کلیدی

پشتیبانی از چند زبان: با استفاده از LANGDETECT و تشخیص زبان متن، چت‌بات از چندین زبان پشتیبانی می‌کند.

تمرکز بر حریم خصوصی: ناشناس‌سازی صدا امنیت داده‌های کاربران را تضمین می‌کند.

شخصی‌سازی صدا: با تبدیل صدا، پاسخ‌های صوتی چت‌بات می‌توانند به شکل دلخواه تنظیم شوند.


===============================================================================

# Text-to-Speech Translation

**Overview**

This project is a text-to-speech translation application that utilizes:

Text translation (using pre-trained translation M2M100 model)

Text-to-speech conversion (via Microsoft Edge TTS)

Language detection
It allows translating text into various languages and converting it into speech.



---

**Features**

Translate text into multiple languages (Persian, English, French, German, Italian ... .)

Convert translated text to audio files and play them automatically

Automatically detect the input text language

Choose the target language for speech output

Download the generated audio file to the Downloads folder



---

**Requirements**

To run this project, you need:

Python 3.8+

Required libraries:

pip install edge-tts nest_asyncio pygame langdetect

Translation models located in the path:
E:\University\master\mbaheseVijeh\project_AI\Translate_\Translate_Models\models



---

**How to Use**

Run the Application

1. Clone the repository:

git clone 
cd 


2. Run the textToSpeech.py file:

python textToSpeech.py


Input

Enter text as input (e.g., "Elle regarde la télévision tous les soirs.").


Output

The translated text in your chosen language.

An audio file named output_File.mp3 will be generated, played automatically, and saved in the Downloads folder.



---

**Project Structure**

main.py: The main script to execute the application

LanguageSelector: A class to select the target speech language

LanguageDetector: A class to detect the language of the input text

TextToSpeechApp: A class to generate and manage the audio file

Speech: A class to handle translation and speech output processes



---

Examples

Input:

Elle regarde la télévision tous les soirs.

Output:

1. Detected language: French


2. Translated text to Persian: او هر شب تلویزیون تماشا می‌کند.


3. Audio file generated and played automatically.




---

**Error Handling**

Possible Issues:

If the translation model is missing from the specified path, the program will not run.

If the selected voice type is unavailable, the default voice (Persian) will be used.




۱.متن به هر زبانی داده شود به زبان فارسی صدا شنیده خواهد شد.(زیرا گفتار سیستم پیش فرض فارسی هست)

مثال:
-متن: Bonjour
صدایی که می شنوید :
سلام

۲.متن به زبان فارسی داده شود و کاربر نوع زبان گفتار را انتخاب کند متن به زبان گفتار مدنظر کاربر شنیده میشود 
مثال: 
متن -سلام 
کاربر تمایل دارد پاسخش به فرانسه شنیده شود در نتیجه Bonjour پخش می شود.



۳.
متن به هر زبانی داده شود و کاربر نوع زبان گفتار را انتخاب کند متن به زبان گفتار مدنظر کاربر شنیده می شود .
مثال :فرض کنید کاربر متن به زبان فرانسه وارد کرده و تمایل دارد پاسخش به زبان انگلیسی باشد.
-متن: Bonjour
صدایی که می شنوید: Hello
۴‌.متن به هر زبانی داده شود و کاربر نوع زبان گفتار را انتخاب نکند یا اشتباه انتخاب کند متن به زبان فارسی شنیده می شود.
مثال
متن-hello

کاربر نوع زبان گفتار را اشتباه انتخاب کرده 
صدایی که پخش می شود: سلام

=========================================================================================================================================================================================================

# Multilingual Translation

**Overview**

This project is a simple and efficient multilingual translation tool built using:

Hugging Face Transformers (M2M100 model for multilingual translation)

Langdetect (for language detection)


The application automatically detects the source language of the input text and translates it into the desired target language using the M2M100 translation model.


---

**Features**

Automatic Language Detection: Detects the source language of the input text using langdetect.

Multilingual Translation: Supports translation between multiple languages.

Hugging Face Integration: Utilizes the M2M100 model for state-of-the-art translation.



---

**Requirements**

Dependencies

Install the required Python libraries:

pip install transformers langdetect torch

Model Setup

Download the M2M100 model and place it in the directory specified in the code:

E:\University\master\mbaheseVijeh\project_AI\Translate_\Translate_Models\models


---

**How to Use**

Running the Script

1. Clone the repository:

git clone 
cd 


2. Run the script:

python main.py



Input

Enter the target language code (e.g., en for English, fr for French, etc.).

Provide the text to translate.


Output

The translated text will be displayed in the console.



---

**Code Overview**

Main Components

1. Translator Class:

Loads the M2M100 model and tokenizer.

Detects the source language of the text.

Translates the text into the target language.



2. get_translation Function:

Simplifies the translation process by initializing the Translator class and returning the translated text.



3. Script Execution:

Prompts the user to input the target language and text.

Displays the translation.





---

Example

Input:

Target Language: en
Text: Bonjour tout le monde.

Output:

Translation: Hello everyone.


---

**Customization**

Model Path: Update the model_path variable to point to the directory where your M2M100 model is stored.

Target Language: Add or modify language codes supported by the M2M100 model.



---

**Error Handling**

Potential Issues

1. Language Detection Error:

If langdetect fails, ensure the input text is long enough for reliable detection.



2. Model Path Error:

Verify that the M2M100 model exists at the specified model_path.



3. Unsupported Language:

Check if the target language is supported by the M2M100 model.


=======================================================================================================================================================================================================================

# Audio Anonymization and Conversion Toolkit

A comprehensive toolset designed for audio file conversion, voice anonymization, and playback, focusing on seamless integration with Python-based audio processing libraries.

## Features
- **Audio Conversion**: Convert between MP3 and WAV formats.
- **Voice Anonymization**: Apply pitch shifting for anonymizing audio recordings.
- **Playback Support**: Play anonymized audio files in MP3 format using `pygame`.
- **Modular Design**: Extendable and reusable code structure for developers.

## Requirements
To run this project, ensure that you have the following libraries installed:

- Python 3.7 or higher
- Required libraries:
  - `librosa` (for audio processing)
  - `soundfile` (for reading and writing WAV files)
  - `pydub` (for audio format conversion)
  - `pygame` (for audio playback)

You can install the necessary dependencies by running:

```bash
pip install -r requirements.txt

Installation and Setup

1. Clone the Repository:

git clone https://github.com/yourusername/audio-anonymization-toolkit.git
cd audio-anonymization-toolkit


2. Install Dependencies: Create and activate a virtual environment, then install the required dependencies:

pip install -r requirements.txt


3. Running the Project: To start processing audio files, run the following command:

python main.py



**Usage**

Convert and Anonymize Audio

You can easily convert and anonymize MP3 files as follows:

from main import process_audio

# Input and output MP3 file paths
input_mp3_file = "input_file.mp3"
output_mp3_file = "anonymized_output.mp3"

# Process the audio
process_audio(input_mp3_file, output_mp3_file)

Play Anonymized Audio

To play the output audio, you can use the play_audio.py script:

python play_audio.py

Customizing the Anonymization

You can modify the pitch_shift_steps parameter in the anonymize_voice function to adjust the degree of anonymization by pitch shifting.

def anonymize_voice(input_file, output_file, pitch_shift_steps=4):
    """Applies pitch shifting to anonymize the audio."""
    # Customize the pitch shift by changing the pitch_shift_steps

**Project Structure**

The project is organized as follows:

├── audio_anonymization.py    # Module responsible for voice anonymization
├── audio_conversion.py       # Module for converting between MP3 and WAV
├── playing_anonymized_sound.py             # Module to handle audio playback
├── requirements.txt          # List of required Python packages
├── anonymize_voice_Main.py                   # Main entry point to process and convert audio

Running Tests

To verify the functionality of the project, run the main.py script, which will handle conversion, anonymization, and playback:

python anonymize_voice_Main.py

==============================================================================================

نحوه عملکرد فایل VoiceConversion

تبدیل صدا با استفاده از مدل SpeechT5-vc

این پروژه از مدل SpeechT5-vc برای تبدیل صدای یک گوینده به صدای گوینده دیگر استفاده می‌کند. مدل SpeechT5-vc مایکروسافت یک مدل پیشرفته برای تبدیل گفتار به گفتار است که می‌تواند صدای گوینده منبع را به صدای گوینده هدف تبدیل کند.همچنین، در این پروژه از xvector برای استخراج ویژگی‌های صدای گوینده استفاده می‌شود که به مدل کمک می‌کند صدای گوینده هدف را شبیه‌سازی کند.

ویژگی‌ها

تبدیل صدای گوینده منبع به صدای گوینده هدف

استفاده از xvector برای استخراج ویژگی‌های صدای گوینده

پشتیبانی از فرمت‌های صوتی مختلف

پخش صدای تبدیل‌شده به صورت آنی

استفاده از مدل SpeechT5 مایکروسافت برای پردازش صدا

نیازمندی‌ها

برای اجرای این پروژه به کتابخانه‌های زیر نیاز دارید:

librosa: برای پردازش صوت

numpy: برای محاسبات عددی

torch: برای مدل‌های PyTorch

pydub: برای دستکاری فایل‌های صوتی

sounddevice: برای پخش صدا

transformers: برای بارگذاری مدل SpeechT5 و پردازشگر آن

torchaudio: برای بارگذاری و پردازش فایل‌های صوتی

=============================================================================================================

**Contact**

For any questions or suggestions:

Email: mahshid.arjmandi.iau@gmail.com

**License**

This project is licensed under the MIT License. See the LICENSE file for more information.


