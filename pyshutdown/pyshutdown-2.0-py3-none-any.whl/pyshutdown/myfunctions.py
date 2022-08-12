import os
def restart(time):
    os.system('shutdown /r /t ' + str(time))
def shutdown(time):
    os.system('shutdown /s /t ' + str(time))