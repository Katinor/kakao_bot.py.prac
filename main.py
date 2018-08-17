#!flask/bin/python
# -*- coding: utf-8 -*-

import random
from functools import wraps
import kakaobot

app = kakaobot.Client(port = 7900)

@app.add_command
def 사잽아():
	return kakaobot.Message(text = "안녕!")

@app.add_prefix_command
def 따라해(content):
	return kakaobot.Message(text = content)

@app.set_extra
def extra_func(content):
	return kakaobot.Message(text = content)

app.run()