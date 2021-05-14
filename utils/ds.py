#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob
import os.path as path

import pathlib

ROOT_DIR = pathlib.Path(__file__).parents[1].joinpath('datasets')

datasets = ROOT_DIR.rglob('*.txt')

def load_all():
	_all = []
	for dataset in datasets:
		words = open(dataset, 'r').read().splitlines()
		for word in words:
			_all.append(word)
	return _all