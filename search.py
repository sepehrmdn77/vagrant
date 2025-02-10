import subprocess
def search(name):
    is_here = subprocess.check_output("vagrant status", shell=True, text=True).split()
    return name in is_here