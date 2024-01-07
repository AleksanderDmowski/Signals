import sys
import subprocess
import pkg_resources


def checking_compatibility_of_packages(fits_exe_relase=False, required_dir={'dir'},info=False):
    its_exe_relase=fits_exe_relase
    if not its_exe_relase:
        required = required_dir
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed

        if missing:
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        else:
            if info:
                print('ok')