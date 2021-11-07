# Built using vscode-ext

import sys
import vscode

ext = vscode.Extension(name = "testpy", display_name = "Test Py", version = "0.0.1")

@ext.event
def on_activate():
	return f"The Extension '{ext.name}' has started"

@ext.command()
def hello_world():
	vscode.window.show_info_message(f'Hello World from {ext.name}')

@ext.command(keybind="ALT+5")
def ask_question():
	res = vscode.window.show_info_message('How are you?', 'Great', 'Meh')
	if res == "Great":
		vscode.window.show_info_message('Woah nice!!')
	elif res == "Meh":
		vscode.window.show_info_message('Sorry to hear that :(')



def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()
