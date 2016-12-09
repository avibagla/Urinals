#!/usr/bin/python
# -*- coding: UTF-8 -*-

#A smattering of useful functions I like to use to simplify things

def get_arguments(arguments, usage=None):
	if len(arguments) % 2 == 0:
		print "each flag specified must have a value"
		if usage:
			print usage
		return {}
	args = {}
	arguments.pop(0)
	while len(arguments)>0:
		flag = arguments.pop(0)
		val = arguments.pop(0)
		args[flag] = val
	return args