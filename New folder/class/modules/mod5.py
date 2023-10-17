import subprocess

def run_command(cmd):
    try: 
        resp = subprocess.check_output(cmd)
        resp = resp.decode('utf-8')
        return resp
    except Exception as e:
        print(f"Unable to run the command : {cmd}")
        print(str(e))


cmd1 = "tasklist"


result = run_command(cmd1)
print(result)

# Actual Args vs Fromal Args
"""
The args which we are passing in fun calling statment those args are called Actual args
The args which are define in fun defiition those args are the fromal args

In above example
cmd1 --> Actual arg
cmd --> formal arg


"""
