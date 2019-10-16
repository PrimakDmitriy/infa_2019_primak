#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
	while not wall_is_on_the_right():
		move_right()
	while not wall_is_on_the_left():
		if not wall_is_above():
			move_up()
		elif not wall_is_beneath():
			move_down()
		move_left()
	if not wall_is_above():
			move_up()
	elif not wall_is_beneath():
		move_down()
	while not wall_is_on_the_left():
		move_left()
	while not wall_is_above():
		move_up()


if __name__ == '__main__':
    run_tasks()
