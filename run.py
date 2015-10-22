#!/usr/bin/python

import sys
import os
import subprocess
import argparse
import time
from machinekit import launcher
from machinekit import rtapi

os.chdir(os.path.dirname(os.path.realpath(__file__)))

parser = argparse.ArgumentParser(description='This is the motorctrl demo run script '
                                 'it demonstrates how a run script could look like '
                                 'and of course starts the motorctrl demo')
parser.add_argument('-nc', '--no_config', help='Disables the config server', action='store_true')
parser.add_argument('-l', '--local', help='Enable local mode only', action='store_true')
parser.add_argument('-g', '--gladevcp', help='Starts the GladeVCP user interface', action='store_true')
parser.add_argument('-s', '--halscope', help='Starts the halscope', action='store_true')
parser.add_argument('-m', '--halmeter', help='Starts the halmeter', action='store_true')
parser.add_argument('-d', '--debug', help='Enable debug mode', action='store_true')

args = parser.parse_args()

if args.debug:
    launcher.set_debug_level(5)

#if not args.local:
#    # override default $MACHINEKIT_INI with a version which was REMOTE=1
#    launcher.set_machinekit_ini('machinekit.ini')


def check_mklaucher():
    try:
        subprocess.check_output(['pgrep', 'mklauncher'])
        return True
    except subprocess.CalledProcessError:
        return False

try:
    launcher.check_installation()
    launcher.cleanup_session()
    launcher.start_realtime()
    launcher.load_hal_file('anddemo.py')
    launcher.register_exit_handler()  # needs to executed after HAL files

    if not check_mklaucher():  # start mklauncher if not running to make things easier
        launcher.start_process('mklauncher .')

    if not args.no_config:
        # the point-of-contact for QtQUickVCP
        launcher.start_process('configserver -n AND-Demo .')
    if args.gladevcp:
        # start the gladevcp version
        if args.local:
            # no -N flag - local case, use IPC sockets, no zeroconf resolution
            launcher.start_process('gladevcp -E -u motorctrl.py motorctrl.ui')
        else:
            # -N - remote case, use zeroconf resolution
            launcher.start_process('gladevcp -N -E -u motorctrl.py motorctrl.ui')
    if args.halscope:
        # load scope only now - because all sigs are now defined:
        launcher.start_process('halscope')
    if args.halmeter:
        launcher.start_process('halmeter')

    while True:
        launcher.check_processes()
        time.sleep(1)

except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)

sys.exit(0)
