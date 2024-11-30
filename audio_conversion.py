from pydub import AudioSegment

class AudioConverter:
    def __init__(self):
        self.audio = None

    def load_audio_from_mp3(self, input_file):
        """بارگذاری فایل صوتی MP3"""
        try:
            self.audio = AudioSegment.from_mp3(input_file)
            print(f"فایل {input_file} با موفقیت بارگذاری شد.")
        except Exception as e:
            print(f"خطا در بارگذاری فایل: {e}")

    def convert_to_wav(self, output_file):
        """ذخیره فایل صوتی به فرمت WAV"""
        if self.audio is not None:
            try:
                self.audio.export(output_file, format="wav")
                print(f"فایل با موفقیت به {output_file} تبدیل شد.")
            except Exception as e:
                print(f"خطا در تبدیل فایل: {e}")
        else:
            print("لطفاً ابتدا فایل صوتی را بارگذاری کنید.")

def convert_wav_to_mp3(input_file, output_file):
    """فایل WAV را به MP3 تبدیل می‌کند."""
    audio = AudioSegment.from_wav(input_file)
    audio.export(output_file, format="mp3")
    print(f"فایل {input_file} به {output_file} تبدیل شد.")