#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import collections
import sys
from useful_functions import get_arguments
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


def main(simulation_runs=100, line_length=100, urinal_number=10):
	print 'Simulation will run', simulation_runs, 'times.'
	print 'There are', urinal_number, 'urinals'
	print 'The line will start with', line_length, 'people'
	cleanest = collections.defaultdict(int)
	dirtiest = collections.defaultdict(int)
	for x in xrange(simulation_runs):
		print 'simulation run:', x
		b = run_simulation(line_length, urinal_number)
		cleanest[b['cleanest']] += 1
		dirtiest[b['dirtiest']] += 1


	print 'cleanest', cleanest
	print 'cleanestest', max(cleanest, key=lambda x: cleanest[x])
	print 'dirtiest', dirtiest
	print 'dirtiestest', max(dirtiest, key=lambda x: cleanest[x])


if __name__ == '__main__':
	usage='''
	python testing.py -s simulation-runs -l line-length -u num-of-urinals
	'''
	if len(sys.argv) > 1:
		arguments = get_arguments(sys.argv, usage)
		if len(arguments) == 3:
		#We'll assume if there are arguments, all three would be specified.
			main(arguments['-s'], arguments['-l'], arguments['-u'])
		else:
			main()

	else:
		main()

