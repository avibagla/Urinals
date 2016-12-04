#!/usr/bin/python
# -*- coding: UTF-8 -*-
import collections

from urinal import Urinal


class Bathroom(object):
	"""A men's bathroom that contains numUrinals of urinals 
	and follows the set of rules provided."""
	def __init__(self, num_urinals, rules_of_play):
		super(Bathroom, self).__init__()
		self.num_urinals = num_urinals
		self.rules_of_play = rules_of_play
		self.urinals = [Urinal() for i in xrange(num_urinals)]
		self.line = collections.deque()
		self.cleanliness="Not enough"

	def __str__(self):
		string = "Bathroom with " + str(self.num_urinals) + " urinals\n"
		string += "The line has " + str(len(self.line)) + " people in it\n"
		string += "The rules of play are the " + self.rules_of_play.__name__
		return string

	def apply_rules(self):
		'''Applies the rules of play to the current urinal set up, and puts
			a person at the urinal in question'''
		if len(self.line) == 0:
			return #If there is no line, then there is no need to apply rules
		urinal_to_use = self.rules_of_play(self.urinals)
		if urinal_to_use is not None:
			self.urinals[urinal_to_use].use_urinal(self.line.popleft())

	def add_person_to_line(self, person):
		self.line.append(person)

	def get_dirtiest_urinal(self):
		urinal = max(self.urinals, key=lambda x: x.number_of_uses())
		return self.urinals.index(urinal)

	def get_cleanest_urinal(self):
		urinal = min(self.urinals, key=lambda x: x.number_of_uses())
		return self.urinals.index(urinal)

	def urinal_use_list(self):
		return [urinal.number_of_uses() for urinal in self.urinals]

	def is_empty(self):
		if bool(self.line):
			return False #there's a line
		for urinal in self.urinals:
			if urinal.is_person_at_urinal():
				return False #Someone is peeing
		return True

	def one_minute_passed(self):
		for urinal in self.urinals:
			urinal.person_urinates()
		for person in self.line:
			person.wait()
		self.apply_rules()

