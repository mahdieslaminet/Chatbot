import librosa
import soundfile as sf

def anonymize_voice(input_file, output_file, pitch_shift_steps=4):
    """فایل WAV را ناشناس‌سازی می‌کند و آن را به فرمت WAV ذخیره می‌کند."""
    samples, sample_rate = librosa.load(input_file, sr=None)

    # اعمال تغییر گام
    samples_shifted = librosa.effects.pitch_shift(samples, sr=sample_rate, n_steps=pitch_shift_steps)

    # ذخیره فایل به عنوان WAV
    sf.write(output_file, samples_shifted, sample_rate)
    print(f"فایل صوتی ناشناس شده با کیفیت بهتر در {output_file} ذخیره شد.")