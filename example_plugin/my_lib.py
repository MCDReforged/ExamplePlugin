from mcdreforged.api.all import *


def register(server: PluginServerInterface):
	server.register_command(Literal('!!cexample').runs(lambda src: src.reply('Hello world from sample command')))
	server.register_help_message('!!example', 'Hello world')
	server.register_help_message('!!cexample', 'Hello world from command')
