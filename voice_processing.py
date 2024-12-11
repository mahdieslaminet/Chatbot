import requests
import json
import wave
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import logging
import asyncio
import pygame
import nest_asyncio
import edge_tts
from huggingface_hub import login
from transformers import pipeline
import os
import textToSpeech
import anonymize_voice_Main
import logging
import playing_anonymized_sound

token = "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"
login(token)


def load_model():
    model_name = "HooshvareLab/gpt2-fa"
    try:
        model = pipeline('text-generation', model=model_name)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Voice Input
def record_audio(filename):
    """Records audio from the microphone and saves it as a WAV file."""
    duration = 5  # Duration in seconds
    fs = 44100  # Sample rate
    logging.info("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    logging.info("Finished recording.")

    # Save the recorded data as a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for int16 format
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())

    logging.info(f"Audio saved as: {filename}")


# Language Detection and Recognition
def recognize_speech(filename):
    """Attempts to recognize speech from an audio file in either Persian or English."""
    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)

    # Try recognizing Persian first
    try:
        text_fa = recognizer.recognize_google(audio_data, language='fa-IR', show_all=True)
        if text_fa:
            best_fa = max(text_fa['alternative'], key=lambda x: x.get('confidence', 0))
            confidence = best_fa.get('confidence', None)
            if confidence is not None and confidence > 0.6:  # Confidence threshold for Persian
                logging.info(f"Recognized Persian Text: {best_fa['transcript']} with confidence: {confidence}")
                return best_fa['transcript'], 'fa'
    except sr.UnknownValueError:
        logging.warning("Could not understand Persian audio.")
    except sr.RequestError as e:
        logging.error(f"Request failed for Persian recognition: {e}")

    # Try recognizing English if Persian recognition fails
    try:
        text_en = recognizer.recognize_google(audio_data, language='en-US', show_all=True)
        if text_en:
            best_en = max(text_en['alternative'], key=lambda x: x.get('confidence', 0))
            confidence = best_en.get('confidence', None)
            if confidence is not None and confidence > 0.6:  # Confidence threshold for English
                logging.info(f"Recognized English Text: {best_en['transcript']} with confidence: {confidence}")
                return best_en['transcript'], 'en'
    except sr.UnknownValueError:
        logging.warning("Could not understand English audio.")
    except sr.RequestError as e:
        logging.error(f"Request failed for English recognition: {e}")

    logging.error("Speech recognition failed for both languages.")
    return None, None  # Return None if both attempts fail


# LLM Integration using HooshvareLab/gpt2-fa
def process_text(question_text):
    """Uses LLM Integration using HooshvareLab/gpt2-fa to process the input text and returns the response."""
    model = load_model()
    response = model(question_text, max_length=100, num_return_sequences=1, temperature=0.9, truncation=True)

    if response:
        # Extract the generated text from the response list
        return response[0]['generated_text']
    else:
        logging.error("No response received from the LLM.")
        return None


#Anonymize
def anonymous(input_user):

    if input_user=='Y':

       #anonymized

       input_mp3_file = "output_File.mp3"  # نام فایل MP3 ورودی
       output_mp3_file = "output_anonymized.mp3"  # نام فایل MP3 خروجی

       anonymize_voice_Main.process_audio(input_mp3_file, output_mp3_file)

       #playing_anonymized_sound
       file_path="output_anonymized.mp3"
       playing_anonymized_sound.main_playing_anonymized_sound(file_path)

    else:#The user does not want the voice to become anonymous.
        print("end.")




# Main Function
def main():
    """Main function to coordinate the workflow."""
    input_filename = 'input.wav'  # The WAV file where the audio input will be saved

    # Step 1: Record audio input
    record_audio(input_filename)

    # Step 2: Recognize speech from the recorded audio
    recognized_text, language = recognize_speech(input_filename)
    if recognized_text:
        logging.info(f"Detected Language: {language}")

    # Step 3: Process the recognized text with the LLM
    processed_text = process_text(recognized_text)


    if processed_text:

        textToSpeech.run_main(processed_text)
        print("Step 4: Convert processed text to speech Sucessful.")


    # step 5:Anonymize the sound by calling the anonymous Method.
    input_user = input("تمایل دارید صدا ناشناس شود؟Y/N")
    print(input_user)
    #calling the anonymous Method.
    anonymous(input_user)



if __name__ == "__main__":
    main()
