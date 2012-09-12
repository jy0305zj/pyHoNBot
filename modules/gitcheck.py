#!/usr/bin/env python
"""
"""

from subprocess import check_output
from os import path

def gitcheck(bot, input):
	"""Am I up-to-date?"""
	if not input.admin: return
	if not path.exists('.git'):
		bot.reply('Not a git repository??')
		return
	args = ['git', 'pull']
	noUpStr = 'Already up-to-date.'
	retStr = check_output(args)
	if retStr.strip() !=  noUpStr:
		bot.reply('Icbot updated. Restarting...')
		bot.close()
		return
	bot.reply('Already up-to-date.')

gitcheck.commands = ['update']