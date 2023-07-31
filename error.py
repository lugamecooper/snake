import os
import os.path
import datetime
import platform

def logs(ER=str):
    logs = open(os.path.join(os.path.dirname(__file__), 
                             f"logs {datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.txt")
                             ,"a")
    logs.write(f'{ER} \n')
    logs.write(f'{platform.machine()} \n')
    logs.write(f'{platform.processor()} \n')
    logs.write(f'{platform.system()} \n')
    logs.write(f'{platform.architecture()} \n')
    logs.write(f'{platform.version()} \n')
    logs.close()
    exit()