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

