import os
import threading

current_path = "C:\\Users\\renat\\OneDrive\\Documentos\\Python\\api"

def env_init():
	os.system(current_path+"\\conf.bat")

thread = threading.Thread(target=env_init)
thread.start()

os.system("start firefox http://localhost:5000")

