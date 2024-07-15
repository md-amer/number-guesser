from random import shuffle
from time import sleep
from os import system
from pyfiglet import Figlet

def msg():
	print('Hi!')
	sleep(1)
	print('Choose a number from 1 to 21 and remember it.')
	sleep(2)
	print('I will ask you thrice to identify the group where your number is present.')
	sleep(3)
	print('And then I will guess it.')
	sleep(3)

msg()

n0 = []

for i in range(1,22):
	n0.append(i)
	
shuffle(n0)
	
a = []
b = []
c = []
n = []
def put_cards(n):
	global a
	global b
	global c
	
	a = [n[0],n[3],n[6],n[9],n[12],n[15],n[18]]
	b = [n[1],n[4],n[7],n[10],n[13],n[16],n[19]]
	c = [n[2],n[5],n[8],n[11],n[14],n[17],n[20]]

put_cards(n0)

def show_groups():
	global a
	global b
	global c
	
	msg()
	print()
	print('A: ',end='')
	for i in range(len(a)):
		if i==len(a)-1:
			print(str(a[i]))
		else:
			print(str(a[i])+', ',end='')

	print('B: ',end='')
	for i in range(len(b)):
		if i==len(b)-1:
			print(str(b[i]))
		else:
			print(str(b[i])+', ',end='')
			
	print('C: ',end='')
	for i in range(len(c)):
		if i==len(c)-1:
			print(str(c[i]))
		else:
			print(str(c[i])+', ',end='')
	print()

w=6
def s(a):
	return w-len(str(a))
	
def msg2():
	print()
	print('Hi!')
	print('Choose a number from 1 to 21 and remember it.')
	print('I will ask you thrice to identify the group where your number is present.')
	print('And then I will guess it.')
	
def show_groups2():
	print()
	print('A'+' '*(w-1)+'B'+' '*(w-1)+'C'+' '*(w-1))
	print(str(a[0])+' '*s(a[0])+str(b[0])+' '*s(b[0])+str(c[0]))
	print(str(a[1])+' '*s(a[1])+str(b[1])+' '*s(b[1])+str(c[1]))
	print(str(a[2])+' '*s(a[2])+str(b[2])+' '*s(b[2])+str(c[2]))
	print(str(a[3])+' '*s(a[3])+str(b[3])+' '*s(b[3])+str(c[3]))
	print(str(a[4])+' '*s(a[4])+str(b[4])+' '*s(b[4])+str(c[4]))
	print(str(a[5])+' '*s(a[5])+str(b[5])+' '*s(b[5])+str(c[5]))
	print(str(a[6])+' '*s(a[6])+str(b[6])+' '*s(b[6])+str(c[6]))
	print()
	
show_groups2()

def regroup():
	select = input('Which group is your number in? ')
	global a
	global b
	global c
	global n
		
	if select == 'A':
		n = b[:]+a[:]+c[:]
		
	if select == 'B':
		n = a[:]+b[:]+c[:]

	if select == 'C':
		n = a[:]+c[:]+b[:]
		
	put_cards(n)
	
regroup()
system('clear')
msg2()
show_groups2()
regroup()
system('clear')
msg2()
show_groups2()
regroup()

print()
print('Your number is',end='')
for i in range(20):
	print('.',end='',flush=True)
	sleep(0.3)
print('.',flush=True)
print(str(b[3]))
f = Figlet(font='doh')
print(f.renderText(str(b[3])))

