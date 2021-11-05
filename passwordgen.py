import random

def generator():
	f = open('passwords.txt', 'w')
	Nombre = int(input('Number of passwords to generate : '))
	Chars = int(input('Length of the password(s) : '))

	for n in range(Nombre):
		motdepasse = ''
		for x in range(Chars):
			motdepasse += random.choice(chr(random.randint(33, 122)))
		print(motdepasse)
		f.write('{}\n'.format(motdepasse))
	print('Saved into passwords.txt')

generator()
