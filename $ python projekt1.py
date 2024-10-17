"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Král
email: petr.kral36@seznam.cz
discord: steel1872
"""
import re
from collections import Counter
from task_template import TEXTS

# Seznam registrovaných uživatelů
registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

def login():
    # Získání uživatelského jména a hesla od uživatele
    username = input("username: ")
    password = input("password: ")
    
    # Ověření, zda jsou přihlašovací údaje správné
    if username in registered_users and registered_users[username] == password:
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
        print("We have 3 texts to be analyzed.")
        print("----------------------------------------")
        return True
    else:
        print(f"username:{username}")
        print(f"password:{password}")
        print("unregistered user, terminating the program..")
        return False

def preprocess_text(text):
    # Odstraníme interpunkci, ale ponecháme čísla
    text = re.sub(r'[^\w\s]', '', text)
    return text

def analyze_text(text):
    clean_text = preprocess_text(text)
    words = clean_text.split()
    
    # Počítání slov
    total_words = len(words)
    
    # Počet slov začínajících velkým písmenem
    capitalized_words = sum(1 for word in words if word[0].isupper())
    
    # Počet slov psaných velkými písmeny
    uppercase_words = sum(1 for word in words if word.isupper() and word.isalpha())
    
    # Počet slov psaných malými písmeny
    lowercase_words = sum(1 for word in words if word.islower())
    
    # Počet čísel (ne cifer)
    numbers = [int(word) for word in words if word.isdigit()]
    total_numbers = len(numbers)
    
    # Suma všech čísel
    sum_numbers = sum(numbers)
    
    # Délky slov
    word_lengths = Counter(len(word) for word in words)
    
    return {
        "total_words": total_words,
        "capitalized_words": capitalized_words,
        "uppercase_words": uppercase_words,
        "lowercase_words": lowercase_words,
        "total_numbers": total_numbers,
        "sum_numbers": sum_numbers,
        "word_lengths": word_lengths
    }

def print_analysis(analysis):
    print(f"There are {analysis['total_words']} words in the selected text.")
    print(f"There are {analysis['capitalized_words']} titlecase words.")
    print(f"There are {analysis['uppercase_words']} uppercase words.")
    print(f"There are {analysis['lowercase_words']} lowercase words.")
    print(f"There are {analysis['total_numbers']} numeric strings.")
    print(f"The sum of all the numbers {analysis['sum_numbers']}")
    print("----------------------------------------")
    
    # Sloupcový graf pro délky slov
    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    max_length = max(analysis['word_lengths'])
    for length in range(1, max_length + 1):
        count = analysis['word_lengths'][length]
        if count > 0:
            print(f"{length:3}|{'*' * count:<13}|{count}")

# Hlavní programová logika
if login():
    # Nabídka textů k analýze
    try:
        choice = int(input("Enter a number btw. 1 and 3 to select: "))
        
        # Kontrola, zda číslo textu odpovídá dostupným textům
        if 1 <= choice <= len(TEXTS):
            print("----------------------------------------")
            selected_text = TEXTS[choice - 1]
            analysis = analyze_text(selected_text)
            print_analysis(analysis)
        else:
            print("Neplatná volba! Program ukončen.")
    except ValueError:
        # Pokud uživatel zadal něco jiného než číslo
        print("Chybný vstup! Prosím, zadejte číslo. Program ukončen.")