import google.generativeai as genai

# Set up your API key
genai.configure(api_key="AIzaSyA2yHCMDL_hGb3cSy-knhZngUmyB8iQtXQ")

def translate_text(text, target_language):
    prompt = f"Translate the following text to {target_language}: {text}"
    
    model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" for general tasks
    
    response = model.generate_content(prompt)
    
    return response.text if response.text else "Translation error"

# Example usage
source_text = "Hello, how are you?"
target_lang = "French"

translated_text = translate_text(source_text, target_lang)
print(f"Translated Text ({target_lang}): {translated_text}")

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    lang = input("Enter target language: ")
    print(f"Translated ({lang}): {translate_text(text, lang)}")

