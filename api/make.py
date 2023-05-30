import os

current_path = os.getcwd()
new_current = ''

for ch in current_path:
    if ch == '\\':
        new_current += '\\'
    new_current += ch

bat_content = '@echo off\n\ncall '+current_path+'\\env\\Scripts\\activate\n\npython '+current_path+'\\src\\main.py\n\n'
py_content = 'import os\nimport threading\n\ncurrent_path = "'+new_current+'"\n\ndef env_init():\n\tos.system(current_path+"\\\\conf.bat")\n\nthread = threading.Thread(target=env_init)\nthread.start()\n\nos.system("start firefox http://localhost:5000")\n\n'
with open('conf.bat', 'w') as bat_file:
    bat_file.write(bat_content)
with open('__init__.py', 'w') as py_file:
    py_file.write(py_content)