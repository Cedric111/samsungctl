#!/usr/bin/env python3

import samsungctl
import time


def printlist():
	print (
	'''
	0  - KEY_POWEROFF    Power off
	1  - KEY_UP  Up
	2  - KEY_DOWN    Down
	3  - KEY_LEFT    Left
	4  - KEY_RIGHT   Right
	5  - KEY_CHUP    P Up
	6  - KEY_CHDOWN  P Down
	7  - KEY_ENTER   Enter
	8  - KEY_RETURN  Return
	9  - KEY_CH_LIST     Channel List
	10 - KEY_MENU    Menu
	11 - KEY_SOURCE  Source
	12 - KEY_GUIDE   Guide
	13 - KEY_TOOLS   Tools
	14 - KEY_INFO    Info
	15 - KEY_RED     A / Red
	16 - KEY_GREEN   B / Green
	17 - KEY_YELLOW  C / Yellow
	18 - KEY_BLUE    D / Blue
	19 - KEY_PANNEL_CHDOWN   3D
	20 - KEY_VOLUP   Volume Up
	21 - KEY_VOLDOWN     Volume Down
	22 - KEY_MUTE    Mute
	23 - KEY_0   0
	24 - KEY_1   1
	25 - KEY_2   2
	26 - KEY_3   3
	27 - KEY_4   4
	28 - KEY_5   5
	29 - KEY_6   6
	30 - KEY_7   7
	31 - KEY_8   8
	32 - KEY_9   9
	33 - KEY_DTV     TV Source
	34 - KEY_HDMI    HDMI Source
	35 - KEY_CONTENTS    SmartHub
	'''
		)

def element(el):
	switcher={
		'0':'KEY_POWEROFF',
		'1':'KEY_UP',
		'2':'KEY_DOWN',
		'3':'KEY_LEFT',
		'4':'KEY_RIGHT',
		'5':'KEY_CHUP',
		'6':'KEY_CHDOWN',
		'7':'KEY_ENTER',
		'8':'KEY_RETURN',
		'9':'KEY_CH_LIST',
		'10':'KEY_MENU',
		'11':'KEY_SOURCE',
		'12':'KEY_GUIDE',
		'13':'KEY_TOOLS',
		'14':'KEY_INFO',
		'15':'KEY_RED',
		'16':'KEY_GREEN',
		'17':'KEY_YELLOW',
		'18':'KEY_BLUE',
		'19':'KEY_PANNEL_CHDOWN',
		'20':'KEY_VOLUP',
		'21':'KEY_VOLDOWN',
		'22':'KEY_MUTE',
		'23':'KEY_0',
		'24':'KEY_1',
		'25':'KEY_2',
		'26':'KEY_3',
		'27':'KEY_4',
		'28':'KEY_5',
		'29':'KEY_6',
		'30':'KEY_7',
		'31':'KEY_8',
		'32':'KEY_9',
		'33':'KEY_DTV',
		'34':'KEY_HDMI',
		'35':'KEY_CONTENTS'
	}
	return switcher.get(el,'unknown')

config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "99",
    "host": "192.168.0.16",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}

with samsungctl.Remote(config) as remote:
	while True:
		printlist()
		keypressed = input("Press key...")
		print (keypressed)
		print (element(keypressed))
		#remote.control("KEY_MENU")
		remote.control(element(keypressed))
