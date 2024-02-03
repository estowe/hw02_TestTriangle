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
    def testNonTriangle(self):
        self.assertEqual(classifyTriangle(4,5,10),'NotATriangle','4,5,10 is not a triangle')
    def testZeroIntegers(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is invalid')
    def testNegativeIntegers(self):
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','-1,-1,-1 is invalid')
    def testEquilateralIsoceles(self):
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','1,1,1 should be equilateral')
    # def testEquilateralScalene(self):
    #     self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    # def testEquilateral(self):
    #     self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    # def testEquilateral(self):
    #     self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    # def testEquilateral(self):
    #     self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    # def testEquilateral(self):
    #     self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')