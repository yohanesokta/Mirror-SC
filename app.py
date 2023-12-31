import customtkinter
from PIL import Image
from tkinter import messagebox
import subprocess
import psutil
from user_data import *
import os
from runner import *

# INTIALIANZING  
window = customtkinter.CTk()
window.title(' Screen Mirroring - Mirror SC')
customtkinter.set_appearance_mode('light')
window.resizable(0,0)


# Open Config Or Write Config
config = load_data()

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
# command button
def full_com():
    global config
    if btn_full.get():
        config.set('User','fullscreen','True')        
    else:
        config.set('User','fullscreen','False')

def audio_com():
    global config
    if btn_audio.get():
        config.set('User','audio','True')
    else:
        config.set('User','audio','False')


def keepOn_com():
    global config
    if btn_on.get():
        config.set('User','keepOn','True')
    else:
        config.set('User','keepOn','False')

def mirror_start():
    global config
    save_data(config)
    cmdUpdate('Starting Screen Mirror\n')
    mainRun(config,window)

def option(btn,name):
    config.set('User',name,btn.get())
    print('update')
    cmdUpdate("setting updated { "+ str(btn.get()) + " }\n")

def option_v(btn,name):
    config.set('User',name,str(int(btn)))
    print('update')
    cmdUpdate("setting updated { "+ str(int(btn)) + " }\n")


def otgM():
    OtgRunner('mouse',window)
def otgMK():
    OtgRunner('key',window)

#TOP LEVEL

def otgConnect():
    top = customtkinter.CTkToplevel()
    lebar = 295
    tinggi = 150
    Width = window.winfo_screenwidth()
    Height = window.winfo_screenheight()
    pos_x = int((Width/2) - (lebar/2))
    pos_y = int((Height/2) - (tinggi/2) - 50)
    top.geometry(f"{lebar}x{tinggi}+{pos_x}+{pos_y}")
    top.resizable(0,0)
    top.title('Select - OTG')
    top.focus_force()
    top.lift()
    top.grab_set()


    mouse = customtkinter.CTkButton(
        master=top,
        width=140,
        height=140,
        fg_color='#1883D5',
        hover_color='#0088FF',
        text='',
        image=customtkinter.CTkImage(Image.open('./asset/mouse.png'),size=(80,82)),
        command=otgM
    )
    mouse.place(x=5,y=5)

    mouse_keyboard = customtkinter.CTkButton(
        master=top,
        width=140,
        height=140,
        fg_color='green',
        hover_color='#60B060',
        text='',
        image=customtkinter.CTkImage(Image.open('./asset/key.png'),size=(80,74)),
        command=otgMK
    )
    mouse_keyboard.place(x=150,y=5)

def AdvanceSetting():
    adv = customtkinter.CTkToplevel()
    adv_global_color = '#006CA3'
    lebar = 290
    tinggi = 400
    Width = window.winfo_screenwidth()
    Height = window.winfo_screenheight()
    pos_x = int((Width/2) - (lebar/2))
    pos_y = int((Height/2) - (tinggi/2) - 50)
    adv.geometry(f"{lebar}x{tinggi}+{pos_x}+{pos_y}")
    adv.resizable(0,0)
    adv.title('Advanced Setings')
    adv.focus_force()
    adv.lift()
    adv.grab_set()
    def top_destroy(args=True):
        if args:
            load_data()
        adv.destroy()
        adv.update()


    def adv_save():
        save_data(config)
        top_destroy(False)

    def no_control():
        if Btn_no_control.get():
            config.set('User','no_control','True')
            if config.get('User','keepon') == 'True':
                messagebox.showwarning('Infone Massehh', 'Mode Keep On Nyala, Fungsi ini tidak dapat bekerja')
                config.set('User','no_control','False')
                Btn_no_control.deselect()
        else:
            config.set('User','no_control','False')

    def no_buffer():
        if Btn_no_buffer.get():
            config.set('User','no_buffer','True')
        else:
            config.set('User','no_buffer','False')

    # Set Wiget ---------------------

    customtkinter.CTkLabel(
        master=adv,
        text="Codec",
        width=290,
        fg_color=adv_global_color,
        text_color='white'
    ).place(x=0,y=0)

    customtkinter.CTkLabel(
        master=adv,
        text='Video'
    ).place(x=15,y=35)

    v_codec = customtkinter.CTkOptionMenu(
        master=adv,
        values=[
            'h264',
            'h265',
            'av1'
        ],
        width=45,
        height=20,
        command=lambda event:option(v_codec,'video_codec')
    )
    v_codec.place(x=55,y=38)

    # Video Bitrate

    customtkinter.CTkLabel(
        master=adv,
        text='Audio'
    ).place(x=lebar-110,y=35)

    a_codec = customtkinter.CTkOptionMenu(
        master=adv,
        values=[
            'opus',
            'aac',
            'raw'
        ],
        width=45,
        height=20,
        command=lambda event:option(a_codec,'audio_codec')
    )
    a_codec.place(x=lebar-70,y=38)


    v_bitrate = 0
    customtkinter.CTkLabel(
        master=adv,
        text='Video Bitrate',
    ).place(x=15,y=70)

    def v_bitrate_change(Val):
        value_v_bitrate.configure(text=str(int(Val/1000)) + ' Kb/s')
        option_v(Val,'v_bitrate')


    btn_slide_vid_bitrate = customtkinter.CTkSlider(
        # default 8000000
        master=adv,
        height=15,
        width=280,
        from_=100000,
        command=v_bitrate_change,
        to=8000000,
    )
    btn_slide_vid_bitrate.place(x=5,y=100)


    customtkinter.CTkLabel(
        master=adv,
        text='Audio'
    ).place(x=lebar-110,y=35)

    #Audio Bitrate

    a_bitrate = 0
    pad_buttom = 50
    customtkinter.CTkLabel(
        master=adv,
        text='Audio Bitrate',
    ).place(x=15,y=70+pad_buttom)

    def a_bitrate_change(Val):
        value_a_bitrate.configure(text=str(int(Val/1000)) + ' Kb/s')
        option_v(Val,'a_bitrate')


    btn_slide_a_bitrate = customtkinter.CTkSlider(
        # default 8000000
        master=adv,
        height=15,
        width=280,
        from_=64000,
        command=a_bitrate_change,
        to=512000,
    )
    btn_slide_a_bitrate.place(x=5,y=100+pad_buttom)
  
    value_a_bitrate = customtkinter.CTkLabel(
        master=adv,
        text=str(int(btn_slide_a_bitrate.get()/1000)) + ' Kb/s',
    )
    value_a_bitrate.place(x=290-70,y=70+pad_buttom)
    

    # Video placing

    # Video Buffer

    v_buffer = 0
    pad_buttom+=70
    customtkinter.CTkLabel(
        master=adv,
        text='Video Buffer',
    ).place(x=15,y=70+pad_buttom)

    def v_buffer_change(Val):
        value_v_buffer.configure(text=str(int(Val)) + ' Kb/s')
        option_v(Val,'v_buffer')

    btn_slide_v_buffer = customtkinter.CTkSlider(
        # default 8000000
        master=adv,
        height=15,
        width=280,
        from_=0,
        command=v_buffer_change,
        to=118,
    )    
    btn_slide_v_buffer.place(x=5,y=100+pad_buttom)

    value_v_buffer = customtkinter.CTkLabel(
        master=adv,
        text=str(int(btn_slide_v_buffer.get())) + ' Kb/s',
    )
    value_v_buffer.place(x=290-70,y=70+pad_buttom)

    # Audio Buffer

    customtkinter.CTkFrame(
        master=adv,
        width=lebar,
        height=1,
        fg_color='black'
    ).place(x=0,y=120)

    # Video Buffer

    pad_buttom+=50
    customtkinter.CTkLabel(
        master=adv,
        text='Audio Buffer',
    ).place(x=15,y=70+pad_buttom)

    def a_buffer_change(Val):
        value_a_buffer.configure(text=str(int(Val)) + ' Kb/s')
        option_v(Val,'a_buffer')

    btn_slide_a_buffer = customtkinter.CTkSlider(
        # default 8000000
        master=adv,
        height=15,
        width=280,
        from_=40,
        command=a_buffer_change,
        to=100,
    )
    btn_slide_a_buffer.place(x=5,y=100+pad_buttom)

    value_a_buffer = customtkinter.CTkLabel(
        master=adv,
        text=str(int(btn_slide_a_buffer.get())) + ' Kb/s',
    )
    value_a_buffer.place(x=290-70,y=70+pad_buttom)


# No Buffer

    Btn_no_buffer = customtkinter.CTkCheckBox(
        master=adv,
        text='No Buffer',
        checkbox_height=14,
        checkbox_width=14,
        border_width=1.5,
        corner_radius=50,
        command=no_buffer
    )
    Btn_no_buffer.place(x=15,y=310)


# No Control

    Btn_no_control = customtkinter.CTkCheckBox(
        master=adv,
        text='No Control',
        checkbox_height=14,
        checkbox_width=14,
        border_width=1.5,
        corner_radius=50,
        command=no_control
    )

    Btn_no_control.place(x=lebar-90,y=310)

    Btn_Adv_Save = customtkinter.CTkButton(
        master=adv,
        text='Save',
        width=100,
        command=adv_save
    )
    Btn_Adv_Save.place(x=25,y=350)

    Btn_Adv_Close = customtkinter.CTkButton(
        master=adv,
        text='Discard',
        width=100,
        fg_color='#FD6262',
        command=top_destroy
    )
    Btn_Adv_Close.place(x=lebar-125,y=350)



    # Set SyncConfig

    syncConfig(v_codec,'video_codec','Option')
    syncConfig(a_codec,'audio_codec','Option')
    syncConfig(btn_slide_vid_bitrate,'v_bitrate','int_Option')
    syncConfig(btn_slide_a_bitrate,'a_bitrate','int_Option')
    syncConfig(btn_slide_v_buffer,'v_buffer','int_Option')
    syncConfig(btn_slide_a_buffer,'a_buffer','int_Option')
    syncConfig(Btn_no_control,'no_control','box')
    syncConfig(Btn_no_buffer,'no_buffer','box')

    value_v_bitrate = customtkinter.CTkLabel(
        master=adv,
        text=str(int(btn_slide_vid_bitrate.get()/1000)) + ' Kb/s',
    )
    value_v_bitrate.place(x=290-70,y=70)

    value_a_bitrate.configure(text=str(int(btn_slide_a_bitrate.get()/1000)) + ' Kb/s')
    value_v_buffer.configure(text=str(int(btn_slide_v_buffer.get())) + ' Kb/s')
    value_a_buffer.configure(text=str(int(btn_slide_a_buffer.get())) + ' Kb/s')

   

# --------------------------------------
# End TOP LEVE:
# --------------------------------------


# Window Wiget  ------------------------


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
    hover_color='#E67E22',
    command=OpenFolder
).place(x=330,y=8)

frame2 = customtkinter.CTkFrame(
    master=window,
    width=480,
    height=200,
    corner_radius=0,
    fg_color='#EBEBEB',
    
).place(x=0,y=60)
                                              
# Screen Mirror
mirror_icon = customtkinter.CTkImage(light_image=Image.open('./asset/mirror.png'),size=(25,22))
btn_mirror = customtkinter.CTkButton(
    master=frame2,                                                                                                                                              
    width=220,
    height=90,
    bg_color='#EBEBEB',
    text='Screen Miror',
    image=mirror_icon,
    command=mirror_start
).place(x=10,y=60)

# Device Mirror
otg_icon = customtkinter.CTkImage(light_image=Image.open('./asset/key.png'),size=(25,23))
btn_otg = customtkinter.CTkButton(
    master=frame2,
    width=220,
    height=97.5,
    text='Device Miror',
    image=otg_icon,
    command=otgConnect
).place(x=10,y=157.5)

color_frame2 = "#A8CDEA"
right_frame2 = customtkinter.CTkFrame(
    master=frame2,
    width=280,
    height=195,
    corner_radius=10,
    fg_color=color_frame2,
    border_color='#484848',
).place(x=240,y=60)

#resolusi layar
res_title = customtkinter.CTkLabel(right_frame2,
    text="Resolution", 
    fg_color=color_frame2,
    bg_color=color_frame2
).place(x=250,y=70)
res_conf = customtkinter.CTkOptionMenu(
    master=right_frame2,
    values=[
        '480p',
        '720p',
        '1080p',
        'Unset'
    ],
    command=lambda event: option(res_conf,'res'),
    bg_color=color_frame2
)
res_conf.place(x=330,y=70)

#framerate setting
frame_title = customtkinter.CTkLabel(
    master=right_frame2,
    text='Frame rate',
    fg_color=color_frame2,
    bg_color=color_frame2,
).place(x=250,y=120)
frame_conf = customtkinter.CTkOptionMenu(
    master=right_frame2,
    values=[
        '30 Fps',
        '50 Fps',
        '60 Fps',
        'Unlock'
    ],
    command=lambda event: option(frame_conf,'mxFps'),
    bg_color=color_frame2
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
    corner_radius=50,
    command=full_com,
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
    corner_radius=50,
    command=audio_com,
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
    corner_radius=50,
    command=keepOn_com,
)
btn_on.place(x=250,y=175)

# record
record_conf = customtkinter.CTkOptionMenu(
    master=right_frame2,
    values=[
        'Not Record',
        'Record (.mp4)',
        'Record (.mkv)'
    ],
    command=lambda event: option(record_conf,'record'),
    bg_color=color_frame2
)
record_conf.place(x=330,y=170)

Adv_image = customtkinter.CTkImage(light_image=Image.open('./asset/setting.png'),size=(20,20))
advance_button = customtkinter.CTkButton(
    master=right_frame2,
    width=32,
    height=32,
    text='',
    bg_color='#EAEAEA',
    image=Adv_image,
    command=AdvanceSetting
)
advance_button.place(x=(480/2)-16,y=10)
cmd = customtkinter.CTkTextbox(
    master=window,
    width=460,
    height= 20,
    bg_color=color_frame2,
    fg_color='#EBEBEB',
    scrollbar_button_color='#EBEBEB',
    scrollbar_button_hover_color='#EBEBEB'
)
cmd.place(x=10,y=470-20)
cmd.insert("0.0",'initializing successfull')
cmd.configure(state='disable')
cmd.unbind()

image_prev = customtkinter.CTkImage(light_image=Image.open('./asset/l_asset_1.png'),size=(460,180))
image_canvas = customtkinter.CTkButton(
    master=window,
    image=image_prev,
    width=460,
    fg_color='#EBEBEB',
    hover_color='#EBEBEB',
    height=180,
    )
image_canvas.place(x=0,y=265)


# --------------------------------------
# End Windows Wiget 
# --------------------------------------

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