from googletrans import Translator

def translate_text(text):
    sentences = text.split('\n')
    translations = []
    translator = Translator()
    translated_sentences_dict = {}
    
    for sentence in sentences:
        if sentence.strip() != "":
            sentence_parts = sentence.split('#')
            original_sentence = sentence_parts[0].strip()
            translations.append("#".join(sentence_parts))
            
            if original_sentence not in translated_sentences_dict:
                translated_sentences_dict[original_sentence] = None
                print(original_sentence)
    translated_sentences = translator.translate(list(translated_sentences_dict.keys()), dest='ko')
    for translation in translated_sentences:
        translated_sentences_dict[translation.origin] = translation.text.strip()
       
    
    for i in range(len(translations)):
        sentence_parts = translations[i].split('#')
        original_sentence = sentence_parts[0].strip()
        translated_sentence = translated_sentences_dict.get(original_sentence, original_sentence)
        translated_sentence = translated_sentence.replace('\n', ' 완료로')
        sentence_parts[0] = f"{original_sentence}#{translated_sentence}"
        translations[i] = "#".join(sentence_parts)
    
    return translations


# Read the content from the before.txt file
with open("after.txt", "r", encoding='utf-8') as file:
    content = file.read()

# Translate the content
translations = translate_text(content)
translated_content = "\n".join(translations)

# Save the translated content to after.txt file
with open("after2.txt", "w", encoding='utf-8') as file:
    file.write(translated_content)

print("번역 결과가 after.txt 파일에 저장되었습니다.")
