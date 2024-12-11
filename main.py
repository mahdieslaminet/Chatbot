from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from langdetect import detect, DetectorFactory

# تنظیم یک دانه برای تکرارپذیری
DetectorFactory.seed = 0

class Translator:
    def __init__(self, model_path, target_lang='en'):
        self.model = M2M100ForConditionalGeneration.from_pretrained(model_path)
        self.tokenizer = M2M100Tokenizer.from_pretrained(model_path)
        self.target_lang = target_lang

    def translate(self, text):
        """
        متن داده‌شده را به زبان مقصد ترجمه می‌کند.

        Args:
            text (str): متنی که باید ترجمه شود.

        Returns:
            str: متن ترجمه‌شده.
        """
        try:
            # تشخیص زبان مبدا
            source_lang = detect(text)
            self.tokenizer.src_lang = source_lang

            encoded_text = self.tokenizer(text, return_tensors="pt")
            generated_tokens = self.model.generate(
                **encoded_text,
                forced_bos_token_id=self.tokenizer.get_lang_id(self.target_lang)
            )
            translated_text = self.tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
            return translated_text
        except Exception as e:
            print(f"خطا در حین ترجمه: {e}")
            return None


def get_translation(model_path, text, target_lang):
    """
    متن را با استفاده از کلاس Translator ترجمه می‌کند.

    Args:
        model_path (str): مسیر به دایرکتوری مدل.
        text (str): متنی که باید ترجمه شود.
        target_lang (str): زبان مقصد برای ترجمه.

    Returns:
        str: متن ترجمه‌شده.
    """
    translator = Translator(model_path, target_lang)
    return translator.translate(text)


if __name__ == "__main__":
    model_path = r"E:\University\master\mbaheseVijeh\project_AI\Translate_\Translate_Models\models"

    # نمونه‌ای از دریافت ورودی از ماژول دیگر
    target_lang = input("لطفا زبان مقصد را وارد کنید (مثلاً 'en' برای انگلیسی): ")
    text = input("لطفا متن را برای ترجمه وارد کنید: ")

    translated_text = get_translation(model_path, text, target_lang)

    # نمایش ترجمه
    if translated_text:
        print("ترجمه:", translated_text)
