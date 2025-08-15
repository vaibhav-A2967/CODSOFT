import random
import string
leng=int(input("Enter the length:"))
characters=string.ascii_letters+string.digits+string.punctuation
password=''.join(random.choice(characters)for i in range(leng))
print("Your Generated Password is :",password)
