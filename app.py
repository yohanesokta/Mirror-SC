import customtkinter
from PIL import Image
import subprocess
import os
import psutil
from user_data import *

# INTIALIANZING  
window = customtkinter.CTk()
window.title('H-Screen Miror')
customtkinter.set_appearance_mode('light')
window.resizable(0,0)

# Open Config Or Write Config
load_data()

# Adb Check
g_adb_running = False
def adbRun():
    if not g_adb_running:
        subprocess.run(['adb.exe','tcpip','5555'], shell = True,cwd='Runtime')
        print('run adb')
        CKAdb()

# check ADB is running or not
def CKAdb():
    process = 'adb.exe'
    process_status = [ proc.status() for proc in psutil.process_iter() if proc.name() == process ]
    if process_status:
        start_adb.configure(
            text='ADB running',
            fg_color='#FFA800',
            hover_color='#FF9200'
        )
        print('Adb running')
        

# window.maxsize & window.minsize

navigation_frame = customtkinter.CTkFrame(
    master=window,
    width=480,
    height=50,
    corner_radius=0,
    fg_color="transparent"
).place(x=0,y=0)


start_adb_icon = customtkinter.CTkImage(light_image=Image.open('./asset/adb.png'),size=(20,24))
start_adb = customtkinter.CTkButton(
    master=navigation_frame,
    text='Start ADB',
    fg_color='#229954',
    height=40,
    text_color='white',
    image=start_adb_icon,
    corner_radius=5,
    hover_color='#52BE80',
    command=adbRun
)
start_adb.place(x=10,y=8)

# Buka folder lokasi
OPL_image = customtkinter.CTkImage(light_image=Image.open('./asset/folder.png'),size=(20,15))
OPL = customtkinter.CTkButton(
    master=navigation_frame,
    text='Open Folder',
    fg_color='#CA6F1E',
    height=40,
    text_color='white',
    image=OPL_image,
    corner_radius=5,
    hover_color='#E67E22'
).place(x=330,y=8)

frame2 = customtkinter.CTkFrame(
    master=window,
    width=480,
    height=200,
    corner_radius=0,
    fg_color='#C7C7C7',
    
).place(x=0,y=60)

# Screen Mirror
mirror_icon = customtkinter.CTkImage(light_image=Image.open('./asset/mirror.png'),size=(25,22))
btn_mirror = customtkinter.CTkButton(
    master=frame2,
    width=220,
    height=80,
    text='Screen Miror',
    image=mirror_icon,
).place(x=10,y=72.5)

# Device Mirror
otg_icon = customtkinter.CTkImage(light_image=Image.open('./asset/key.png'),size=(25,23))
btn_otg = customtkinter.CTkButton(
    master=frame2,
    width=220,
    height=80,
    text='Device Miror',
    image=otg_icon
).place(x=10,y=167.5)

color_frame2 = "#DBDBDB"
right_frame2 = customtkinter.CTkFrame(
    master=frame2,
    width=280,
    height=200,
    corner_radius=0,
    bg_color='#C7C7C7'
).place(x=240,y=60)

#resolusi layar
res_title = customtkinter.CTkLabel(right_frame2,
    text="Resolution", 
    fg_color=color_frame2
).place(x=250,y=70)
res_conf = customtkinter.CTkOptionMenu(
    master=right_frame2,
    values=[
        '1280x720',
        '1920x1080'
    ]
).place(x=330,y=70)

#framerate setting
frame_title = customtkinter.CTkLabel(
    master=right_frame2,
    text='Frame rate',
    fg_color=color_frame2
).place(x=250,y=120)
frame_conf = customtkinter.CTkOptionMenu(
    master=right_frame2,
    values=[
        '30 fps',
        '50 fps',
        '60 fps',
        'max framerate'
    ]
).place(x=330,y=120)

#fullscreen
btn_full = customtkinter.CTkCheckBox(
    master=right_frame2,
    text='FullScreen',
    bg_color=color_frame2,
    height=18,
    checkbox_height=14,
    checkbox_width=14,
    border_width=1.5,
    corner_radius=50
).place(x=250,y=220)

#audio
btn_audio = customtkinter.CTkCheckBox(
    master=right_frame2,
    text='Audio forward',
    bg_color=color_frame2,
    height=18,
    checkbox_height=14,
    checkbox_width=14,
    border_width=1.5,
    corner_radius=50
).place(x=360,y=220)

# stay awake

btn_on = customtkinter.CTkCheckBox(
    master=right_frame2,
    text='Keep ON',
    bg_color=color_frame2,
    height=18,
    checkbox_height=14,
    checkbox_width=14,
    border_width=1.5,
    corner_radius=50
).place(x=250,y=175)

# record
record_conf = customtkinter.CTkOptionMenu(
    master=right_frame2,
    values=[
        'Not Record',
        'Record (.mp4)',
        'Record (.mkv)'
    ]
).place(x=330,y=170)

# test
# s = subprocess.check_output("scrcpy.exe", shell = True)
# print(s.decode("utf-8"))

# p = subprocess.Popen(["scrcpy.exe"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# output, errors = p.communicate()

# print(output)

# test

# Start Checking Adb
process = 'adb.exe'
process_status = [ proc.status() for proc in psutil.process_iter() if proc.name() == process ]
if process_status:
    g_adb_running = True
    start_adb.configure(
            text='ADB running',
            fg_color='#FFA800',
            hover_color='#FF9200'
            )


#setingan layar
lebar = 480
tinggi = 480
sWidth = window.winfo_screenwidth()
sHeight = window.winfo_screenheight()
pos_x = int((sWidth/2) - (lebar/2))
pos_y = int((sHeight/2) - (tinggi/2) - 50)
window.geometry(f"{lebar}x{tinggi}+{pos_x}+{pos_y}")
window.mainloop()