#!/bin/bash
coverage run test_triangle.py
coverage report -m > coverage_results.txt
