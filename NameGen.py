import re
import random

genNum = 40

domain = "@email.com"

firstname = []
firstname_txt = open('C:/Users/vwimmer/Documents/Git/Tests/firstnames.txt', 'r')
for firstnames in firstname_txt:
	firstnames = firstnames.strip('\n')
	firstname.append(firstnames)
firstname_txt.close()

lastname = []
lastname_txt = open('C:/Users/vwimmer/Documents/Git/Tests/lastnames.txt', 'r')
for lastnames in lastname_txt:
	lastnames = lastnames.strip('\n')
	lastname.append(lastnames)
lastname_txt.close()

gN = 0
email = ""

while gN in range(genNum):
	x = random.randint(0, (len(firstname) - 1))
	fn = firstname[x]

	y = random.randint(0, (len(lastname) - 1))
	ln = lastname[y]

	z = random.randint(0, 9)

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

	print(fn,ln)
	print(email)
	print("--------------------------------")

	gN = gN + 1
