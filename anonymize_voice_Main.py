from audio_anonymization import anonymize_voice
from audio_conversion import AudioConverter, convert_wav_to_mp3

def process_audio(mp3_file, anonymized_mp3_file):
    """فرآیند کامل تبدیل، ناشناس‌سازی و تبدیل مجدد به MP3 را انجام می‌دهد."""
    wav_file = "temp_audio.wav" # فایل موقت WAV

    # تبدیل MP3 به WAV
    converter = AudioConverter()
    converter.load_audio_from_mp3(mp3_file)
    converter.convert_to_wav(wav_file)

    # ناشناس‌سازی فایل WAV
    anonymized_wav_file = "anonymized_audio.wav" # فایل ناشناس‌سازی شده
    anonymize_voice(wav_file, anonymized_wav_file)

    # تبدیل فایل ناشناس‌سازی شده به MP3
    convert_wav_to_mp3(anonymized_wav_file, anonymized_mp3_file)
    print("convert_wav_to_mp3 sucessful.")



# مثال استفاده

if __name__ == "__main__":

    input_mp3_file = "output_File.mp3" # نام فایل MP3 ورودی
    output_mp3_file = "output_anonymized.mp3" # نام فایل MP3 خروجی
    process_audio(input_mp3_file, output_mp3_file)