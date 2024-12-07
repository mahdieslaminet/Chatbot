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

Text-to-Speech Translation

Overview

This project is a text-to-speech translation application that utilizes:

Text translation (using pre-trained translation models)

Text-to-speech conversion (via Microsoft Edge TTS)

Language detection
It allows translating text into various languages and converting it into speech.



---

Features

Translate text into multiple languages (Persian, English, French, German, Italian)

Convert translated text to audio files and play them automatically

Automatically detect the input text language

Choose the target language for speech output

Download the generated audio file to the Downloads folder



---

Requirements

To run this project, you need:

Python 3.8+

Required libraries:

pip install edge-tts nest_asyncio pygame langdetect

Translation models located in the path:
E:\University\master\mbaheseVijeh\project_AI\Translate_\Translate_Models\models



---

How to Use

Run the Application

1. Clone the repository:

git clone <repository-url>
cd <repository-folder>


2. Run the main.py file:

python main.py



Input

Enter text as input (e.g., "Elle regarde la télévision tous les soirs.").


Output

The translated text in your chosen language.

An audio file named output_File.mp3 will be generated, played automatically, and saved in the Downloads folder.



---

Project Structure

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

Error Handling

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


=======================================================================================================================================================================================================================

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





