#!/bin/bash
# Counts the number of Java code lines in a directory
find . -type f -name '*.py' | xargs wc -l