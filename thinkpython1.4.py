#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  thinkpython1.4.py
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
#
#if you run a 10 k.m. race in 43 minute 30 seconds , what is your
#average time per mile?
#what is your average speed in miles per hour?

time = float(input()) #transforming it to floating number
distance = int(input()) #python in default takes input in string
distance_in_mile = distance / 1.61
print("the distance in mile", distance_in_mile,".")
print("the average time is ", time / distance_in_mile, ".")
print("the average speed is", distance / time * 60, ".")
