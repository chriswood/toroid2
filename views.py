#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Chris Wood on 2010-08-17.
Copyright (c) 2010 __All Things Chris Wood__. All lefts reserved.
"""

import sys
import os
from django.http import HttpResponse

def main(request):
	return(HttpResponse("Now it's on"))


if __name__ == '__main__':
	main()

