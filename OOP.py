#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s score is %s' % (self.name, self.score))



class
tom = Student('tom', '100')

tom.print_score()
