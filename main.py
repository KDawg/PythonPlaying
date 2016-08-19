# learn python in 5 minutes: https://learnxinyminutes.com/docs/python/
# Learn Python: http://www.learnpython.org/en/Welcome

import math
import pprint
import player_model

print 'hello world'

count = 10
color_choices = ['red', 'green', 'blue', 42, 'black', 'white']
is_on = True
order = {
  'first_name': 'Norman',
  'last_name': 'Rockwell'
}

order['product_name'] = 'keyboard'
order['product_id'] = '87d4ff60-63f7-11e6-8b77-86f30ca893d3'
order['count'] = 1

print 'a dictionary (aka hash) look like this:'
print order
pprint.pprint(order)
print order.keys()
print order.values()
print order['product_id']
print '\n'
print color_choices
print 'the color_choices array has [%d] elements in it ' % len(color_choices)

if 'magenta' in color_choices:
  print 'a secondary color is available'

if 'green' in color_choices:
  print 'a primary color is available'

if 'orange' in color_choices:
  print 'a seconday color is available'
else:
  print 'there is no secondary color'

print 'the second color choice is [%s]' % color_choices[2]

for color in color_choices:
  print 'a color choice is [%s]' % color


def graph(m, theta_zero, theta_one):
  print '\ngraph h(x) = %s + %s' % (str(theta_zero), str(theta_one))
  for i in range(m):
    h(i, theta_zero, theta_one)


def h(index, theta_zero, theta_one):
  ans = theta_zero + theta_one * index
  print ans


graph(count, 0.5, 1.5)
graph(count, 0.0, 0.25)

print '\n'
print 'the constant value of pi from the math library is [%s]' % math.pi
for i in range(0, 10):
  print 'sqrt of [%i] is [%f]' % (i, math.sqrt(i))


player1 = player_model.Player(first_name='Ken', last_name='Tabor', handle='KDawg')
print '\n'
print player1.first_name
print player1.last_name
player1.print_full_name()
