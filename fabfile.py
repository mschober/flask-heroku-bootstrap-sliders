#!/usr/bin/env python

from fabric.api import *

def run():
    local('python app.py')

def browser():
    local('chrome "http://localhost:5000/sliders"')


