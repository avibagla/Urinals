#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import collections
from bathroom import Bathroom
from urinal import Urinal
from person import Person



def normal_rules(urinal_array):
	def is_urinal_usable(index):
		#Checks to see if the urinal is taken, or if it is next to a taken urinal
		if bool(urinal_array[index].is_person_at_urinal()):
			return False
		if index == 0:
			return not bool(urinal_array[index + 1].is_person_at_urinal() )
		if index == len(urinal_array) - 1:
			return not bool(urinal_array[index - 1].is_person_at_urinal() )
		return (not bool(urinal_array[index + 1].is_person_at_urinal())) and (not bool(urinal_array[index - 1].is_person_at_urinal() ))
	urinal_usability_list = [is_urinal_usable(x) for x in xrange(len(urinal_array))]
	if (sum([int(x) for x in urinal_usability_list])) == 0:
		#The original rules don't give us any urinals
		#so we need to choose any of the open urinals
		urinal_usability_list = [not bool(u.is_person_at_urinal()) for u in urinal_array]
	if (sum([int(x) for x in urinal_usability_list])) == 0:
		#there are *no* urinals open. Like, every single one is taken.
		return None
	#Now, let's make this unnecessarily complicated to prove my understanding of
	#programming to you
	list_of_open_urinals = [pair[0] for pair in zip(xrange(len(urinal_array)), urinal_usability_list) if pair[1]]
	return random.choice(list_of_open_urinals)


def choose_any_open_urinals(urinal_array):
	#This is for those fuckers who ignore urinal rules and just choose a urinal
	#regardless if there is someone in the urinal next to them.
	urinal_usability_list = [not x.is_person_at_urinal() for x in urinal_array]
	list_of_open_urinals = [pair[0] for pair in zip(xrange(len(urinal_array)), urinal_usability_list) if pair[1]]
	return random.choice(list_of_open_urinals)

def run_simulation(line_length=100, urinals_in_bathroom=10):	
	brom = Bathroom(urinals_in_bathroom, normal_rules)

	[brom.add_person_to_line(Person(random.choice(xrange(2,6)))) for x in range(line_length)]

	while not brom.is_empty():
		brom.one_minute_passed()

	return {
		'cleanest': brom.get_cleanest_urinal(),
		'dirtiest': brom.get_dirtiest_urinal(),
		'total uses': brom.urinal_use_list()}


def main():
	cleanest = collections.defaultdict(int)
	dirtiest = collections.defaultdict(int)
	for x in xrange(100):
		b = run_simulation(1000)
		cleanest[b['cleanest']] += 1
		dirtiest[b['dirtiest']] += 1


	print 'cleanest', cleanest
	print 'dirtiest', dirtiest

main()



	
