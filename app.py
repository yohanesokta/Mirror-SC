import customtkinter
from PIL import Image
import subprocess
import os
import psutil
from user_data import *

    # 0.scrcpy.exe - default on runtime
    # 1.fulscreen
    # 2.audo forward
    # 3.keep on 
    # 4.resulusi
    # 5.frame rate
    # 6.record

# INTIALIANZING  
window = customtkinter.CTk()
window.title('H-Screen Miror')
customtkinter.set_appearance_mode('light')
window.resizable(0,0)
# Open Config Or Write Config
config = save_data()


def cmdUpdate(add):
    cmd.configure(state='normal')
    cmd.insert("0.0",add)
    cmd.configure(state='disable')

# Adb Check
g_adb_running = False
def adbRun():
    if not g_adb_running:
        run = subprocess.run(['adb.exe','tcpip','5555'], shell = True,cwd='Runtime')
        cmdUpdate('program started adb.exe\n')
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
        '480p',
        '720p',
        '1080p'
    ]
)
res_conf.place(x=330,y=70)

#framerate setting
frame_title = customtkinter.CTkLabel(
    master=right_frame2,
    text='Frame rate',
    fg_color=color_frame2
).place(x=250,y=120)
frame_conf = customtkinter.CTkOptionMenu(
    master=right_frame2,
    values=[
        '30 Fps',
        '50 Fps',
        '60 Fps',
        'Unlock'
    ]
)
frame_conf.place(x=330,y=120)

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
)
btn_full.place(x=250,y=220)

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
)
btn_audio.place(x=360,y=220)

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
)
btn_on.place(x=250,y=175)

# record
record_conf = customtkinter.CTkOptionMenu(
    master=right_frame2,
    values=[
        'Not Record',
        'Record (.mp4)',
        'Record (.mkv)'
    ]
)
record_conf.place(x=330,y=170)

cmd = customtkinter.CTkTextbox(
    master=window,
    width=460,
    height= 20,
    fg_color='transparent',
    scrollbar_button_color='#EBEBEB',
    scrollbar_button_hover_color='#EBEBEB'
)
cmd.place(x=10,y=470-20)
cmd.insert("0.0",'initializing successfull')
cmd.configure(state='disable')
cmd.unbind()
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
    cmdUpdate('adb.exe is already running\n')
    g_adb_running = True
    start_adb.configure(
            text='ADB running',
            fg_color='#FFA800',
            hover_color='#FF9200'
            )

# Sync Aplikasi dengan save data config
syncConfig(btn_full,'fullscreen','box')
syncConfig(btn_audio,'audio','box')
syncConfig(btn_on,'keepOn','box')
syncConfig(res_conf,'res','Option')
syncConfig(frame_conf,'MxFps','Option')
syncConfig(record_conf,'record','Option')

#setingan layar
lebar = 480
tinggi = 480
sWidth = window.winfo_screenwidth()
sHeight = window.winfo_screenheight()
pos_x = int((sWidth/2) - (lebar/2))
pos_y = int((sHeight/2) - (tinggi/2) - 50)
window.geometry(f"{lebar}x{tinggi}+{pos_x}+{pos_y}")
window.mainloop()