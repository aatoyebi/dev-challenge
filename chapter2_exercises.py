# Exercises for chapter 2:

# Name: Amaka Atoyebi

#2.1

print 5

x = 5

print x + 1

#2.2

val1 = 01
val2 = 010
val3 = 0100
val4 = 01000

print (val1)
print (val2)
print (val3)
print (val4)

#2.3

# 8
# 8.5
# 4.0
# 11
#.....

#2.4
#1
pi = 3.14
r = 5**3

vol = (4*pi*r)/3

print (vol)

#2
cp = 24.95
perc = .4
first = 3
add = 0.75
books = 60

disc = cp - (perc * cp)

total = (disc * books) + (add * 59) + 3

print (total)

#3
first_mile = (8*60) + 15
three_miles = (7*60 + 12) * 3
last_mile = first_mile
separator = ':'

total_time = (first_mile + three_miles + last_mile)

my_hour = total_time/3600
my_min = total_time/60
my_sec = total_time - (my_min * 60)

hour_left = 6 + my_hour
min_left = 52 + my_min

if(min_left > 60):
	hour_left = hour_left + 1
	min_left = min_left - 60

if(my_sec < 10):
    my_sec = '0' + str(my_sec)

time_arrived = str(hour_left) + separator + str(min_left) + separator + str(my_sec)

print (time_arrived)
