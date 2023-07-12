import subprocess
from tkinter import messagebox
from pathlib import Path
import time
import os
home = str(Path.home())
os.system('mkdir '+ home + '\\videos\\MirrorRec\\')
rec_path = home + '\\videos\\MirrorRec\\MirrorRec_' + str(time.time())


def mainRun(args,window):
    global home
    rec_path = home + '\\videos\\MirrorRec\\MirrorRec_' + str(time.time())
    lib = 'User'
    exec = ['scrcpy.exe']
    if args.get(lib,'fullscreen') == 'True':
        exec += ['-f']
    if args.get(lib,'audio') == 'False':
        exec += ['--no-audio']
    if args.get(lib,'keepOn') == 'True':
        exec += ['-w']
    
    match args.get(lib,'res'):
        case '480p':
            exec += ['--max-size=480']
        case '720p':
            exec += ['--max-size=720']
        case '1080p':
            exec += ['--max-size=1080']

    match args.get(lib,'mxFps'):
        case '30 Fps':
            exec += ['--max-fps=30']
        case '50 Fps':
            exec += ['--max-fps=50']
        case '60 Fps':
            exec += ['--max-fps=60']

    match args.get(lib,'record'):
        case 'Record (.mp4)':
            exec += ['-r',rec_path + '.mp4']
        case 'Record (.mkv)':
            exec += ['-r',rec_path + '.mkv']
    print(exec)
    window.withdraw()
    try:
        grepOut = subprocess.check_output(exec, shell=True,cwd='Runtime')                       
    except subprocess.CalledProcessError as grepexc:                                                                                                   
        messagebox.showerror('Program Gak iso jalan', 'Please check cable or turn on USB Debugging')
    window.deiconify()


# function otg

def OtgRunner(hid,window):
    exec = ['scrcpy.exe','--otg','-M']
    if hid == 'key':
        exec += ['-K']
    try:
        prog = subprocess.check_output(exec,shell=True,cwd='Runtime')
    except subprocess.CalledProcessError as progexc:
        messagebox.showerror('Program Gak iso jalan', 'Please check cable or turn on USB Debugging')

def OpenFolder():
    subprocess.Popen(['explorer.exe',home + '\\videos\\MirrorRec'])