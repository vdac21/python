#Actual Args vs Formal Args
"""The args which we are passing in fun calling statement those args are called Actual args

The args which are define in fun defination those args are the formal args"""


import subprocess

def run_command(cmd):
    try:
        resp=subprocess.check_output(cmd)
        resp=resp.decode('utf-8')
        return resp
    except Exception as e:
        print(f"unable to run the command:{cmd}")
        print(str(e))

cmd1 ="tasklist"

result=run_command(cmd1)
print(result)
