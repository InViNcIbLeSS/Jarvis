import asyncio
import websockets
import os
import sys
import webbrowser
import config_data
sys.path.append(config_data.jarvis_folder_location)
from jarvisBrain import Brain
from classifier.jarvisClassifierN import JarvisClassifier
from command_manager import CommandManager
import pyttsx
from JarvisN.database.datahelper import DataDbHelper
engine = pyttsx.init('sapi5')

def speak(speech):
	engine.say(speech)
	engine.runAndWait()
	print('Spoke')

def main():
	
	
	os.chdir(config_data.directory_path)
	#webbrowser.open('http://localhost/jarvis/jarvis.php')
	java_path = "C:\Program Files\Java\jdk1.8.0_101\\bin\java.exe"
	os.environ['JAVAHOME'] = config_data.java_path
	brain = Brain()
	classifier = JarvisClassifier()
	commandManager = CommandManager()
	#db = DataDbHelper()
	
	while(True):
	
		msg = input()
		#cmd = brain.getCommand(msg)
		cmd = classifier.classify(msg,'general')
		sub = classifier.classify(msg,cmd)
		
		#React
		entity , type = commandManager.callCommand(cmd, msg)
		print(cmd,sub,entity,type)
		if msg == " close" or msg == "close":
			break
	print("closed")
			
		
		
	

if __name__ == "__main__":
	main()