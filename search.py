import subprocess
def search(name):
    is_here = subprocess.check_output("vagrant status", shell=True, text=True).split()
    return name in is_here

def check():
    mutual_list = ['saved','running','Current', 'machine', 'states:', 'poweroff', '(virtualbox)', 'poweroff', '(virtualbox)', 'This', 'environment', 'represents', 'multiple', 'VMs.', 'The', 'VMs', 'are', 'all', 'listed', 'above', 'with', 'their', 'current', 'state.', 'For', 'more', 'information', 'about', 'a', 'specific', 'VM,', 'run', '`vagrant', 'status', 'NAME`.']
    checking = subprocess.check_output("vagrant status", shell=True, text=True).split()
    result = ''
    for item in checking:
        if item not in mutual_list:
            result += f'\n{item}\n'
    return result