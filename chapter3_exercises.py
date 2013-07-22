# Exercises for chapter 3:

# Name: Amaka Atoyebi

#3.1

'''repeat_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

def repeat_lyrics():
	print_lyrics()
	print_lyrics()'''

#3.2

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."	

repeat_lyrics()

#3.3

def right_justify(s):
	spaceLength = 70 - len(s)
	spaceBefore = spaceLength * ' '
	print spaceBefore + s

right_justify('allen')	

#3.4

def do_twice(f, v):
	f(v)
	f(v)

def print_spam():
	print 'spam'

def print_twice(s):
	print s
	print s

def do_four(f, v):	
	do_twice(f, v)
	do_twice(f, v)


do_twice(print_twice, 'spam')	
do_four(print_twice, 'spam')	


