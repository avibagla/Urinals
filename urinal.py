#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Urinal(object):
	"""docstring for Urinal"""
	def __init__(self):
		super(Urinal, self).__init__()
		self.__uses = 0
		self.__person_at_urinal = None

	def use_urinal(self, person):
		self.__person_at_urinal = person
		self.__uses += 1

	def is_person_at_urinal(self):
		return bool(self.__person_at_urinal)

	def __leave_urinal(self):
		self.__person_at_urinal = None

	def person_urinates(self):
		if self.__person_at_urinal:
			self.__person_at_urinal.urinate()
			if self.__person_at_urinal.is_bladder_empty():
				self.__leave_urinal()

	def number_of_uses(self):
		return self.__uses