#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, glob
import os.path as path

import pathlib

ROOT_DIR = pathlib.Path(__file__).parents[1].joinpath('datasets')

def load_all():
	datasets = ROOT_DIR.rglob('*.txt')
	_all = []
	for dataset in datasets:
		words = open(dataset, 'r').read().splitlines()
		for word in words:
			_all.append(word)
	return _all

def load_dataset(directory):
	datasets = ROOT_DIR.joinpath(directory).rglob('*.txt')
	_all = []
	for dataset in datasets:
		words = open(dataset, 'r').read().splitlines()
		for word in words:
			_all.append(word)
	return _all
