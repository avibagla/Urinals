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

def run_long_line_simulation(line_length=100, urinals_in_bathroom=10):	
	brom = Bathroom(urinals_in_bathroom, normal_rules)

	[brom.add_person_to_line(Person(5)) for x in range(line_length)]

	while not brom.is_empty():
		brom.one_minute_passed()

	return {
		'cleanest': brom.get_cleanest_urinal(),
		'dirtiest': brom.get_dirtiest_urinal(),
		'total uses': brom.urinal_use_list()
		}


def main(simulation_runs=100, line_length=100, number_of_urinals=10, verbose=False):
	print 'Simulation will run', simulation_runs, 'times.'
	print 'There are', number_of_urinals, 'urinals'
	print 'The line will start with', line_length, 'people'
	cleanest_urinal_dictionary = collections.defaultdict(int)
	dirtiest_urinal_dictionary = collections.defaultdict(int)
	total_uses_overall = [0]*number_of_urinals
	for x in xrange(simulation_runs):
		if verbose: print 'simulation run:', x
		b = run_long_line_simulation(line_length, number_of_urinals)
		cleanest_urinal_dictionary[b['cleanest']] += 1
		dirtiest_urinal_dictionary[b['dirtiest']] += 1
		total_uses_overall = [sum(x) for x in zip(total_uses_overall, b['total uses'])]

	print '-'*80
	cleanest_urinal_overall = max(cleanest_urinal_dictionary, key=lambda x: cleanest_urinal_dictionary[x])
	dirtiest_urinal_overall = max(dirtiest_urinal_dictionary, key=lambda x: dirtiest_urinal_dictionary[x])
	print_str = '''Typically, the {0} urinal was urinal {1} with {2} occurrences as the {0} urinal\nUrinal {1} had an average of {3} uses'''
	print print_str.format('cleanest', cleanest_urinal_overall, 
		cleanest_urinal_dictionary[cleanest_urinal_overall], 
		float(total_uses_overall[cleanest_urinal_overall])/simulation_runs)
	print print_str.format('dirtiest', dirtiest_urinal_overall, 
		dirtiest_urinal_dictionary[dirtiest_urinal_overall], 
		float(total_uses_overall[dirtiest_urinal_overall])/simulation_runs)
	print '-'*80
	print 'Average uses per urinal'
	for x in range(number_of_urinals):
		print x, ':', float(total_uses_overall[x])/simulation_runs
	


if __name__ == '__main__':
	usage='''
	python testing.py -s simulation-runs -l line-length -u num-of-urinals
	'''
	if len(sys.argv) > 1:
		arguments = get_arguments(sys.argv, usage)
		if len(arguments) == 3:
		#We'll assume if there are arguments, all three would be specified.
			main(int(arguments['-s']), int(arguments['-l']), int(arguments['-u']))
		else:
			main()
	else:
		main()

