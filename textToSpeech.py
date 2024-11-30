import edge_tts
import asyncio
import nest_asyncio
import os
import pygame
from main import get_translation
from langdetect import detect, DetectorFactory
import time

nest_asyncio.apply()


async def main(text, target_lang):
    model_path = r"E:\University\master\mbaheseVijeh\project_AI\Translate_\Translate_Models\models"

    # ترجمه متن
    translated_text = get_translation(model_path, text, target_lang)

    # نمایش ترجمه
    if translated_text:
        print(f"متن اصلی: {text}")
        print(f"ترجمه به زبان گفتار: {translated_text}")

    return translated_text


class TextToSpeechApp:
    def __init__(self, text):
        self.text = text # دریافت متن از ورودی
        self.output_file = "output_File.mp3"

        # تولید صدا و پخش خودکار
        asyncio.run(self.generate_audio(self.text))

    async def generate_audio(self, text, voice="fa-IR-faridNeural"):
        # استفاده از صدای FaridNeural
        self.text_speech = text
        self.voice_speech = voice
        communicate = edge_tts.Communicate(self.text_speech, self.voice_speech)

        try:
            await communicate.save(self.output_file)
            print("فایل با موفقیت ذخیره شد.")
            self.play_audio() # پخش خودکار صدا پس از تولید
        except Exception as e:
            print("خطا در ذخیره فایل:", e)

    def play_audio(self):
        if os.path.exists(self.output_file):
            try:
                # پخش فایل صوتی با استفاده از pygame
                pygame.mixer.init()
                pygame.mixer.music.load(self.output_file)
                pygame.mixer.music.play()
                print("صدا در حال پخش است...")

                # انتظار برای پایان پخش صدا
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)  # با زمان کوتاه منتظر ماندن تا پایان پخش

                # آزادسازی منابع پس از پخش صدا
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                print("منابع آزاد شد.")

            except Exception as e:
                print(f"Error loading or playing audio: {e}")
        else:
            print("File does not exist.")

    def download_audio(self):
        if os.path.exists(self.output_file):
            try:
                import shutil
                shutil.copy(self.output_file, os.path.expanduser("~/Downloads"))
                print("File downloaded to Downloads folder.")
            except Exception as e:
                print(f"Error downloading file: {e}")
        else:
            print("File does not exist.")


class LanguageSelector:
    def __init__(self):
        self.languages = [
            {'fa': 'fa-IR-faridNeural'},
            {'en': 'en-US-faridNeural'},
            {'fr': 'fr-FR-faridNeural'},
            {'de': 'de-DE-faridNeural'},
            {'it': 'it-IT-faridNeural'}
        ]
        self.selected_language = None # متغیر برای ذخیره زبان انتخاب شده

    def main(self):
        print("تمایل دارید پاسختان را به چه زبانی دریافت کنید؟ از بین زبان ها انتخاب نمایید:")
        print("en-US-faridNeural, fa-IR-faridNeural, fr-FR-faridNeural, de-DE-faridNeural, it-IT-faridNeural")

        # دریافت مقدار انتخابی از کاربر
        self.target_lang_ = input("\nاز بین زبان های نام برده شده انتخاب نمایید: ")

        # جستجو در لیست دیکشنری‌ها
        self.selected_language = None # برای ذخیره کلید یافت‌شده

        for d in self.languages:
            for key, value in d.items():
                if value == self.target_lang_:
                    self.selected_language = key
                    break
            if self.selected_language: # اگر کلید پیدا شد، از حلقه خارج می‌شویم
                break

        # چاپ کلید مربوط به مقدار واردشده
        if self.selected_language:
            print("نوع زبان مدنظر شما جهت گفتار:", self.selected_language)
        else: # اگر نوع زبان گفتار پیدا نشد به طور پیش فرض فارسی در نظر گرفته شود
            self.selected_language = 'fa'
            print("زبانی که مدنظر شما است به زودی پشتیبانی می شود در حال حاضر این زبان توسط تیم پشتیبانی نشده است.")


class LanguageDetector:
    def __init__(self):
        pass

    def detect_language(self, text):
        """تشخیص زبان یک متن و برگرداندن آن"""
        if not text: # بررسی اینکه آیا متن ورودی خالی است
            print("متن ورودی خالی است.")
            return None

        try:
            language = detect(text) # تشخیص زبان
            return language # برگرداندن زبان تشخیص داده شده
        except Exception as e:
            print(f"خطا در تشخیص زبان: {e}")
            return None # در صورت خطا، None برگردانده می‌شود


class Speech:
    def __init__(self, select_voice_type_=None, generated_text=None):
        self.select_voice_type_ = select_voice_type_
        self.generated_text = generated_text # ذخیره متن تولید شده

    def compression(self):
        self.class_detector_instance = LanguageDetector()
        text_type = self.class_detector_instance.detect_language(self.generated_text)
        if text_type: # اگر زبان تشخیص داده شده وجود داشته باشد
            print(f"زبان متن: {text_type}") # چاپ زبان تشخیص داده شده
        else:
            print("تشخیص زبان ناموفق بود.") # در صورت عدم موفقیت در تشخیص

    def print_speech_type(self):
        if self.select_voice_type_:
            print(f"نوع زبان گفتار: {self.select_voice_type_}")
            self.translated_text = asyncio.run(main(self.generated_text, self.select_voice_type_))
            return self.translated_text
        else:
            return 0 # اگر نوع زبان گفتار مشخص نشد


def run_main(generated_text):
    # برای انتخاب نوع زبان گفتار
    selector = LanguageSelector()
    selector.main()
    select_voice_type = selector.selected_language

    # اگر نوع زبان گفتار مشخص شد
    speech1 = Speech(select_voice_type, generated_text) # ارسال متن به کلاس Speech
    translated_text_speech1 = speech1.print_speech_type()

    # صدا تولید شو
    app = TextToSpeechApp(translated_text_speech1)

    # تشخیص زبان متن
    detector = LanguageDetector()
    text_type = detector.detect_language(generated_text)
    if text_type: # اگر زبان تشخیص داده شده وجود داشته باشد
        print(f"زبان متن: {text_type}") # چاپ زبان تشخیص داده شده
    else:
        print("تشخیص زبان ناموفق بود.") # در صورت عدم موفقیت در تشخیص


# اجرای برنامه و ارسال متن تولید شده به کلاس
if __name__ == "__main__":
    generated_text = "Elle regarde la télévision tous les soirs."
    run_main(generated_text)

