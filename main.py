#!flask/bin/python
# -*- coding: utf-8 -*-

import random
from functools import wraps
import kakaobot

# 먼저 Cliend 객체를 하나 선언합니다. 포트는 제 서버 환경 기준입니다.
app = kakaobot.Client(port = 7900)

# add_command 데코레이터는 자신에게 전달된 배열을 커맨드로 등록합니다.
# 전달된 배열이 없다면 자신이 꾸미는 함수의 이름을 커맨드로 등록합니다.
@app.add_command()
def 하이루(user_key):
	return kakaobot.Message(text = "안녕!")

@app.add_command(["안녕","반가워"])
def greeting(user_key):
	return kakaobot.Message(text = "나도 반가워!")

# add_prefix_command 데코레이터는 자신에게 전달된 배열을 커맨드로 등록합니다.
# 배열이 전달되지 않았을 경우, 자신이 꾸미는 함수의 이름을 커맨드로 등록합니다.
# 챗봇이 받은 말이 이 데코레이터로 등록된 표현으로 시작한다면 챗봇이 반응합니다.
@app.add_prefix_command()
def 따라해(user_key, content):
	return kakaobot.Message(text = content)

@app.add_prefix_command(["말해봐"])
def temp_pref_comm(user_key, content):
	return kakaobot.Message(text = content)

# add_regex_command 데코레이터는 자신에게 전달된 정규식 표현을 커맨드로 등록합니다.
# 챗봇이 받은 말이 이 데코레이터로 등록된 정규식 표현에 매칭된다면 챗봇이 반응합니다.
# 예시의 경우에는 "사잽아 <문자열> 따라해" 라는 말을 들으면, 그 사람에게 "<문자열>" 이라고 답하는 기능입니다.
@app.add_regex_command('^사잽아 ((?:(?! 따라해).)*) 따라해')
def regex_func(user_key,content):
	return kakaobot.Message(text = content[0])

# set_extra 데코레이터는 위의 경우를 제외하고 나머지의 경우에 수행되는 함수를 등록합니다.
@app.set_extra
def extra_func(user_key, content):
	return kakaobot.Message(text = content)

# set_friend_add_event 데코레이터는 누군가 챗봇을 친구로 등록했을 때 동작하는 함수를 등록합니다.
@app.set_friend_add_event
def temp_func_a(user_key):
	print("Friend_add : "+str(user_key))

# set_friend_delete_event 데코레이터는 누군가 챗봇을 친구목록에서 제외했을 때 동작하는 함수를 등록합니다.
@app.set_friend_delete_event
def temp_func_b(user_key):
	print("Friend_del : "+str(user_key))

# set_chatroom_leave_event 데코레이터는 누군가 챗봇과의 채팅방을 나갔을때 동작하는 함수를 등록합니다.
@app.set_chatroom_leave_event
def temp_func_c(user_key):
	print("chat_leave : "+str(user_key))

# 마지막으로 run() 메소드를 사용하면 끝납니다.
app.run()