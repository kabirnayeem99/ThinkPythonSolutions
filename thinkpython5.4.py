#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  thinkpython5.4.py
#  
#  Copyright 2019 Kabir Nayeem <kabirnayeem.99@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

#  write a function called do_n 
#  that takes a object function &
#  a number, n, as arguements and
#  that calls the given functions 
#  n times
print("Think Python \n Excercise 5.4")
print("write a function called do_n"),
print("that takes a object and a number, n, as arguements and that calls"),
print("the given functions n times\n")

print("Here is your writing.")
def do_n(func, n):
	if n == 0:
		print("You are done.\n Thank you")
	else:
		func(x)
		do_n(func, n - 1)

def print_s(x):
	print(x)

x = str(input("What do you want to write: "))	
n = int(input("& How many times: "))

func = print_s	

do_n(func, n)
