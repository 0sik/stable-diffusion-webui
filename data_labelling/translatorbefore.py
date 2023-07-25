

def translate_text(text):
    sentences = text.split('\n')
    translations = []
    
    for sentence in sentences:
        if sentence.strip() != "":
            sentence_parts = sentence.split('#')
            original_sentence = sentence_parts[0].strip()
            translations.append("#".join(sentence_parts))
            print("번역중")
        else:
            if translations:  # Check if there are any translations
                print("하나완료")
                translations.append("완료로")
    
    return translations


# Read the content from the before.txt file
with open("before.txt", "r", encoding='utf-8') as file:
    content = file.read()

# Translate the content
translations = translate_text(content)
translated_content = "\n".join(translations)

# Save the translated content to after.txt file
with open("after.txt", "w", encoding='utf-8') as file:
    file.write(translated_content)

print("번역 결과가 after.txt 파일에 저장되었습니다.")
