#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Person(object):
	"""docstring for Person"""
	def __init__(self, initial_bladder_fullness):
		super(Person, self).__init__()
		self.__bladder_fullness = initial_bladder_fullness


	def urinate(self):
		if self.__bladder_fullness < 1:
			self.__bladder_fullness = 0
		else:
			self.__bladder_fullness -= 1

	def is_bladder_empty(self):
		return not bool(self.__bladder_fullness)

	def wait(self):
		self.__bladder_fullness += 0.1