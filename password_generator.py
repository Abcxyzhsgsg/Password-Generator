import random
import string
def password_generator(length=12):
    character=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(character)for i in range(length))
    return password
password=password_generator
print("generated password", password)
