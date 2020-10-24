import random
import string

s1=''.join((random.choice(string.ascii_letters) for i in range(6)))
s1+=''.join((random.choice(string.digits) for i in range(4)))
s1+=''.join((random.choice(string.punctuation) for i in range(2)))

new_list=list(s1)
random.shuffle(new_list)
password=''.join(new_list)

print(password)