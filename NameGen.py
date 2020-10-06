import re
import random

genNum = 40

domain = "@email.com"

email = ""

firstname = []
firstname_txt = open('firstnames.txt', 'r')
for firstnames in firstname_txt:
	firstnames = firstnames.strip('\n')
	firstname.append(firstnames)
firstname_txt.close()

lastname = []
lastname_txt = open('lastnames.txt', 'r')
for lastnames in lastname_txt:
	lastnames = lastnames.strip('\n')
	lastname.append(lastnames)
lastname_txt.close()

adjective = []
adjective_txt = open('adjectives.txt', 'r')
for adjectives in adjective_txt:
	adjectives = adjectives.strip('\n')
	adjective.append(adjectives)
adjective_txt.close()

noun = []
noun_txt = open('nouns.txt', 'r')
for nouns in noun_txt:
	nouns = nouns.strip('\n')
	noun.append(nouns)
noun_txt.close()

gN = 0

while gN in range(genNum):
	f = random.randint(0, (len(firstname) - 1))
	fn = firstname[f]

	l = random.randint(0, (len(lastname) - 1))
	ln = lastname[l]

	a1 = random.randint(0, (len(adjective) - 1))
	adj1 = adjective[a1]

	a2 = random.randint(0, (len(adjective) - 1))
	adj2 = adjective[a2]

	n1 = random.randint(0, (len(noun) - 1))
	noun1 = noun[n1]

	n2 = random.randint(0, (len(noun) - 1))
	noun2 = noun[n2]

	z = random.randint(0, 14)

	year = random.randint(1969, 1994)

	num = random.randint(22, 500)

	if z == 0:
		email = str(fn + ln + domain).lower()

	if z == 1:
		email = str(fn[0] + ln + domain).lower()

	if z == 2:
		email = str(fn + ln[0] + domain).lower()

	if z == 3:
		email = str(fn + ln[0] + str(year) + domain).lower()

	if z == 4:
		email = str(fn + ln[0] + str(num) + domain).lower()

	if z == 5:
		email = str(fn + ln + str(year) + domain).lower()

	if z == 6:
		email = str(fn + ln + str(num) + domain).lower()

	if z == 7:
		email = str(fn[0] + ln + str(year) + domain).lower()

	if z == 8:
		email = str(fn[0] + ln + str(num) + domain).lower()

	if z == 9:
		email = str(fn[0] + fn[1] + fn[2] + ln[0] + str(num) + domain).lower()

	if z == 10:
		email = str(adj1 + fn + str(num) + domain).lower()

	if z == 11:
		email = str(adj1 + fn + str(year) + domain).lower()

	if z == 12:
		email = str(adj1 + noun1 + noun2 + domain).lower()

	if z == 13:
		email = str(adj1 + noun1 + str(num) + adj2 + noun2 + domain).lower()

	if z == 14:
		email = str(fn + noun2 + str(num) + domain).lower()

	if z == 13:
		email = str(adj1 + noun1 + adj2 + noun2 + str(num) + domain).lower()

	print(fn,ln)
	print(email)
	print("--------------------------------")

	gN = gN + 1
