import random as rd
import string


def generate_password(request):
    password = []
    characters = [string.ascii_lowercase]
    j = 1
    
    if request.GET.get('numbers'):
        characters.append(string.digits)
        j += 1

    if request.GET.get('uppercase'):
        characters.append(string.ascii_uppercase)
        j += 1
    
    if request.GET.get('special-characters'):
        characters.append(string.punctuation)
        j += 1

    i = 0
    length = request.GET.get('length', 12)
    while i < int(length):
        character = rd.choice(characters[i % j])
        password.append(character)
        i += 1
    
    rd.shuffle(password)
    return ''.join(password)
