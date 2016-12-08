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





	
