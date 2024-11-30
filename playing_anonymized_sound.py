import pygame

# ماژول برای راه‌اندازی pygame
def initialize_pygame():
    pygame.mixer.init()
    print("Pygame initialized.")

# ماژول برای بارگذاری فایل MP3
def load_mp3(file_path):
    pygame.mixer.music.load(file_path)
    print(f"Loaded: {file_path}")

# ماژول برای پخش voice 
def play_music():
    pygame.mixer.music.play()
    print("Playing output_anonymized...")

# ماژول برای بررسی وضعیت پخش صدا
def wait_until_music_ends():
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    print("Voice has finished playing.")

# ماژول اصلی برای اجرای برنامه
def main_playing_anonymized_sound(file_path):
    # راه‌اندازی pygame
    initialize_pygame()

    # بارگذاری فایل MP3
    load_mp3(file_path)

    # پخش voice
    play_music()

    # منتظر ماندن تا پایان voice
    wait_until_music_ends()

if __name__ == "__main__":
    # بارگذاری فایل MP3
    file_path = "output_anonymized.mp3"
    main_playing_anonymized_sound(file_path)
