import librosa
import numpy as np
import torch
from pydub import AudioSegment
import sounddevice as sd
from transformers import SpeechT5Processor, SpeechT5ForSpeechToSpeech, SpeechT5HifiGan
checkpoint = "microsoft/speecht5_vc"
processor = SpeechT5Processor.from_pretrained(checkpoint)
model = SpeechT5ForSpeechToSpeech.from_pretrained(checkpoint)
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

speaker_embeddings = {
    "BDL": r"E:\University\master\mbaheseVijeh\Sound_AI\cmu_us_bdl_arctic-wav-arctic_a0009.npy",
    "CLB": r"C:\Users\mahshidaa\Desktop\Voice_Conversion\xvector.npy",
    "KSP": "/home/lenovo/Jarvis/spkrec-xvect/cmu_us_ksp_arctic-wav-arctic_b0087.npy",
    "RMS": "/home/lenovo/Jarvis/spkrec-xvect/cmu_us_rms_arctic-wav-arctic_b0353.npy",
    "SLT": "/home/lenovo/Jarvis/spkrec-xvect/cmu_us_slt_arctic-wav-arctic_a0508.npy",
}

def process_audio(sampling_rate, waveform):
    # convert from int16 to floating point
   # waveform = waveform / 32678.0

    # convert to mono if stereo
    if len(waveform.shape) > 1:
        waveform = librosa.to_mono(waveform.T)

    # resample to 16 kHz if necessary
    if sampling_rate != 16000:
        waveform = librosa.resample(waveform, orig_sr=sampling_rate, target_sr=16000)

    # limit to 30 seconds
    waveform = waveform[:16000*30]

    # make PyTorch tensor
    waveform = torch.tensor(waveform)
    return waveform

import torchaudio

def load_audio(file_path):
    try:
        # Load the audio file
        waveform, sample_rate = librosa.load(file_path)
        return sample_rate, waveform
    except Exception as e:
        print(f"Error loading audio: {str(e)}")
        return None, None

def predict(audio, mic_audio=None):
    # audio = tuple (sample_rate, frames) or (sample_rate, (frames, channels))
    if mic_audio is not None:
        sampling_rate, waveform = mic_audio
    elif audio is not None:
        sampling_rate, waveform = load_audio(audio)
    else:
        return (16000, np.zeros(0).astype(np.int16))

    waveform = process_audio(sampling_rate, waveform)
    inputs = processor(audio=waveform, sampling_rate=16000, return_tensors="pt")
    speaker_embedding = np.load(r"C:\Users\mahshidaa\Desktop\Voice_Conversion\xvector.npy")#Xvector فایل صوتی گوینده هدف

    print("Original speaker embeddings shape:", speaker_embedding.shape)

    # تبدیل به Tensor و اصلاح ابعاد
    speaker_embedding= torch.tensor(speaker_embedding).squeeze(1)  # حذف بعد اضافی
    print("After squeeze:", speaker_embedding.shape)


    print(speaker_embedding.shape)
    print(f"Input shape: {inputs['input_values'].shape}")

    #تولید صدا
    speech = model.generate_speech(inputs["input_values"], speaker_embedding, vocoder=vocoder)
    print(f"Input shape: {inputs['input_values'].shape}")

    #speech = (speech.numpy() * 32767).astype(np.int16)
    audio = AudioSegment(
        data=speech.numpy(),
        sample_width=1,  # 16-bit audio
        frame_rate=16000,
        channels=1  # 1 channel for mono audio
    )
    # Play the audio using sounddevice
    sd.play(audio.raw_data, samplerate=16000)
    sd.wait()


predict(audio=r"E:\University\master\mbaheseVijeh\Voice_Conversion\librispeech_dev_clean\LibriSpeech\dev-clean\1462\170138\1462-170138-0000.flac")#audio=>فایل صوتی منبع که متن مهم است.
