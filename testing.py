#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import collections
from bathroom import Bathroom
from urinal import Urinal
from person import Person
from rules import normal_rules, choose_any_open_urinals

def run_simulation(line_length=100, urinals_in_bathroom=10):	
	brom = Bathroom(urinals_in_bathroom, normal_rules)

	[brom.add_person_to_line(Person(5)) for x in range(line_length)]

	while not brom.is_empty():
		brom.one_minute_passed()

	return {
		'cleanest': brom.get_cleanest_urinal(),
		'dirtiest': brom.get_dirtiest_urinal(),
		'total uses': brom.urinal_use_list()
		}


def main():
	cleanest = collections.defaultdict(int)
	dirtiest = collections.defaultdict(int)
	for x in xrange(100):
		print 'simulation run:', x
		b = run_simulation(100)
		cleanest[b['cleanest']] += 1
		dirtiest[b['dirtiest']] += 1


	print 'cleanest', cleanest
	print 'cleanestest', max(cleanest, key=lambda x: cleanest[x])
	print 'dirtiest', dirtiest
	print 'dirtiestest', max(dirtiest, key=lambda x: cleanest[x])

main()