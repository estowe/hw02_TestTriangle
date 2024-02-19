# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from Triangle import classifyTriangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testZeroIntegers(self):
        self.assertEqual(classifyTriangle(201,201,201),'Input greater than 200','201,201,201 is invalid')
    def testNegativeIntegers(self):
        self.assertEqual(classifyTriangle(-1,-1,-1),'Input less than 0','-1,-1,-1 is invalid')
    def testNonIntegers(self):
        self.assertEqual(classifyTriangle(1.5,1.5,1.5),'Input not integer','1.5,1.5,1.5 is invalid')
    def testEquilateralIsoceles(self):
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be equilateral')
    def testRight(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 should be right')
    def testScalene(self):
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 should be scalene')
    def testIsoceles(self):
        self.assertEqual(classifyTriangle(3,4,4),'Isoceles','3,4,4 should be isoceles')
    def testNonTriangle(self):
        self.assertEqual(classifyTriangle(4,5,10),'NotATriangle','4,5,10 is not a triangle')