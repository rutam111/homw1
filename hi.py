def karaca_encrypt(text):
    
    reversed_text = text[::-1]
    
    translation_table = str.maketrans('aeiou', '01230')
    replaced_text = reversed_text.translate(translation_table)

    encrypted_text = replaced_text + 'aca'
    
    return encrypted_text

print(karaca_encrypt("banana"))
print(karaca_encrypt("karaca"))  
print(karaca_encrypt("burak"))  
print(karaca_encrypt("alpaca"))
