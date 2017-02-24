#!/usr/bin/env python
import urllib2, extra, time, os, urllib, subprocess, json
from main import wake


""" THIS IS WHERE ALL THE COMMAND ARE STORED """


global par1
par1 = "bacpac"

def bye():
    while True:
        sure = str(raw_input("\r\n[" + extra.colors.cyan + "*" + extra.colors.end + "] Are you sure you wanna quit? [Y/N] : "))
        if sure == "Y" or sure == "y":
            print("\r\n["+extra.colors.cyan+"*"+extra.colors.end+"] Bye ;)")
            time.sleep(1)
            subprocess.call(["clear"])
            os._exit(1)
        elif sure == "N" or sure == "n":
            print("")
            break

def help():

    """DEFINING ALL COMMANS FOR HELP FUNCTION"""

    commands = {0:"on - Turn on your camera",1:"off - Turn off your camera",2:"shoot - Emulation of the shoot button(start video, take pic, ecc..",\
                3:"stop_rec - Stop recording",4:"no_leds - Turn off all the leds on your camera",5:"preview_on - Turn preview mode on",6:"preview_off - Turn preview mode off",\
                7:"video - Put your camera in video mode",8:"photo - Put your camera in photo mode",9:"brust - Put your camera in brust mode",10:"timelapse - Put your camera in timelapse mode",\
                11:"timer - Put your camera in timer mode",12:"play_hdmi - Put your camera in play mode (if connected to monitor)", 13:"orientation_up - Move the camera orientation up",\
                14:"orientation_down - Move the camera orientation down",15:"fov_wide - Put the FOV in wide mode ( FOV = Field Of View )",16:"fov_medium - Put the FOV in medium mode",\
                17:"fov_narrow - Put the FOV in narrow mode",18:"mute - Put the volume to 0%",19:"volume_70 - Put the volume to 70%", 20:"volume_100 - Put the volume to 100%",\
                21:"protune_on - Turn the protune mode on",22:"protune_off - Turn the protune mode off", 23:"2_leds - Switch 2 leds on", 24:"4_leds - Switch 4 leds on",\
                25:"autopoweroff \"option\" - Set autopoweroff (options: nev = never, 60s, 120s, 300s)"}

    #DEFINIGN SPECIAL COMMANDS
    special_cmds = {0:"stealth_mode - Your GoPro becomes invisble (all leds off, mute on and wide FOV)",1:"stealth_mode_off - Turn stealth mode off",2:"shoot&get - Take a picture and download it"}
    print("\r\n\t| "+extra.colors.yellow+"All PyHero Commands :"+extra.colors.end+" |")
    print("\t ----------------------")
    for command in commands:
        print("\t| "+commands[command])
    print("\n\t| " + extra.colors.green + "PyHero Special Commands :" + extra.colors.end + " |")
    print("\t ----------------------")
    for super_command in special_cmds:
        print("\t| " + special_cmds[super_command])
    print("\r\n")


""" HERE IS WHERE ALL THE WIRELESS COMMANDS ARE STORED, ALL THE IF STATEMENTS YOU SEE ARE
    USED IN ORDER TO CHANGE THE CONTENT OF THE COMMAND BASED ON THE CAMERA """

def on(passwd, camera): #TURN ON THE GOPRO
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Turning the GoPro on")
    if not passwd :
        if camera == "HERO4 Session":
            return("http://10.5.5.9/gp/gpControl/setting/10/1", False, False)
        else :
            wake(camera)
            print("\r\n[" + extra.colors.green + "+" + extra.colors.end + "] Command executed successfully ;)\r\n")
            return(False, False, False)
    else :
        par2= "PW"
        opt = "01"
        return(par1, par2, opt)

def off(passwd, camera): #TURN OFF THE GOPRO
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Turning the GoPro off")
    if not passwd :
        if camera == "HERO4 Session":
            return("http://10.5.5.9/gp/gpControl/setting/10/0", False, False)
        else :
            return("http://10.5.5.9/gp/gpControl/command/system/sleep", False, False)
    else :
        par2 = "PW"
        opt = "00"
        return (par1, par2, opt)

def shut(): #START RECORDING/TAKING PHOTO ecc..
    par2 = "SH"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Pressing the shoot button")
    return (par1, par2, opt)

def stop(): #STOP VIDEO
    par2 = "SH"
    opt = "00"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Stopping the video")
    return (par1, par2, opt)

def no_leds(): #SHUT THE CAMERA'S LED DOWN
    par2 = "LB"
    opt = "00"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Turning the leds off")
    return (par1, par2, opt)

def prev_on(): #PREVIEW ON
    global par1
    par1 = "camera"
    par2 = "PV"
    opt = "02"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Turning preview on")
    return (par1, par2, opt)

def prev_off():  #PREVIEW OFF
    global par1
    par1 = "camera"
    par2 = "PV"
    opt = "00"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Turning preview off")
    return (par1, par2, opt)

def video_mode():  #VIDEO MODE
    global par1
    par1 = "camera"
    par2 = "CM"
    opt = "00"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing to video mode")
    return (par1, par2, opt)

def photo_mode():  #PHOTO MODE
    global par1
    par1 = "camera"
    par2 = "CM"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing to photo mode")
    return (par1, par2, opt)

def brust_mode():  #BRUST MODE
    global par1
    par1 = "camera"
    par2 = "CM"
    opt = "02"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing to brust mode")
    return (par1, par2, opt)

def timelapse_mode():  #TIMELAPSE MODE
    global par1
    par1 = "camera"
    par2 = "CM"
    opt = "03"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing to timelapse mode")
    return (par1, par2, opt)

def timer_mode():  #TIMER MODE
    global par1
    par1 = "camera"
    par2 = "CM"
    opt = "04"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing to timer mode")
    return (par1, par2, opt)

def play_hdmi():  #PLAY ON HDMI (IF CONNECTED)
    global par1
    par1 = "camera"
    par2 = "CM"
    opt = "05"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Playing on HDMI port")
    return (par1, par2, opt)

def or_up():  #ORIENTATION UP
    global par1
    par1 = "camera"
    par2 = "UP"
    opt = "00"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Moving the orientation up")
    return (par1, par2, opt)

def or_down():  #ORIENTATION DOWN
    global par1
    par1 = "camera"
    par2 = "UP"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Moving the orientation down")
    return (par1, par2, opt)

def fov_wide():  #WIDE FOV
    global par1
    par1 = "camera"
    par2 = "FV"
    opt = "00"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing the FOV to wide mode")
    return (par1, par2, opt)

def fov_med():  #MEDIUM FOV
    global par1
    par1 = "camera"
    par2 = "FV"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing the FOV to medium mode")
    return (par1, par2, opt)

def fov_nar():  #NARROW FOV
    global par1
    par1 = "camera"
    par2 = "FV"
    opt = "02"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing the FOV to narrow mode")
    return (par1, par2, opt)

def no_vol():  #NO VOLUME(MUTE)
    global par1
    par1 = "camera"
    par2 = "BS"
    opt = "00"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing volume to mute")
    return (par1, par2, opt)

def vol_70(): #VOLUME 70%
    global par1
    par1 = "camera"
    par2 = "BS"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing volume to 70%")
    return (par1, par2, opt)

def vol_100():  #VOLUME 100%
    global par1
    par1 = "camera"
    par2 = "BS"
    opt = "02"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Changing volume to 100%")
    return (par1, par2, opt)

def pro_on():   #PROTUNE ON
    global par1
    par1 = "camera"
    par2 = "PT"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Putting protune on")
    return (par1, par2, opt)

def pro_off():  #PROTUNE OFF
    global par1
    par1 = "camera"
    par2 = "PT"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Putting protune off")
    return (par1, par2, opt)

def leds2():  #2 LEDS ON
    global par1
    par1 = "camera"
    par2 = "LB"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Switching to 2 leds on")
    return (par1, par2, opt)

def leds4():  #4 LEDS ON
    global par1
    par1 = "camera"
    par2 = "LB"
    opt = "02"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Switching to 4 leds on")
    return (par1, par2, opt)

def autoN():  #AUTO POWER OFF: NEVER
    global par1
    par1 = "camera"
    par2 = "AO"
    opt = "00"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Setting auto power off to never")
    return (par1, par2, opt)

def auto60():   #AUTO POWER OFF: 60s
    global par1
    par1 = "camera"
    par2 = "AO"
    opt = "01"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Setting auto power off to 60s")
    return (par1, par2, opt)

def auto120():  #AUTO POWER OFF: 120s
    global par1
    par1 = "camera"
    par2 = "AO"
    opt = "02"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Setting auto power off to 120s")
    return (par1, par2, opt)

def auto300():  #AUTO POWER OFF: 300s
    global par1
    par1 = "camera"
    par2 = "AO"
    opt = "03"
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Setting auto power off to 300s")
    return (par1, par2, opt)

##SPECIAL COMMANDS

def stealth_mode(passwd):
    df = "http://10.5.5.9/"  # DEFAULT PARTS
    p1 = "?t="
    p2 = "&p=%"

    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Activating stealth mode")

    par1, par2, opt = no_vol()  # MUTE MODE
    urllib2.urlopen(df + par1 + "/" + par2 + p1 + passwd + p2 + opt)
    time.sleep(1.5)

    par1, par2, opt = no_leds()  # NO LEDS
    urllib2.urlopen(df + par1 + "/" + par2 + p1 + passwd + p2 + opt)
    time.sleep(1.5)

    par1, par2, opt = fov_wide()  # FOV WIDE FOR A BIGGER FIELD OF VIEW
    urllib2.urlopen(df + par1 + "/" + par2 + p1 + passwd + p2 + opt)
    time.sleep(1.5)

    print("\r\n[" + extra.colors.green + "+" + extra.colors.end + "] Stealth mode activated successfully\r\n")

def stealth_off(passwd):
    df = "http://10.5.5.9/"  # DEFAULT PARTS
    p1 = "?t="
    p2 = "&p=%"

    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Deactivating stealth mode")

    par1, par2, opt = vol_100()  # MUTE MODE
    urllib2.urlopen(df + par1 + "/" + par2 + p1 + passwd + p2 + opt)
    time.sleep(1.5)

    par1, par2, opt = leds4()  # NO LEDS
    urllib2.urlopen(df + par1 + "/" + par2 + p1 + passwd + p2 + opt)
    time.sleep(1.5)

    print("\r\n[" + extra.colors.green + "+" + extra.colors.end + "] Stealth mode deactivated successfully\r\n")
def getLast(passwd):
    df = "http://10.5.5.9/" #DEFAULT PARTS
    p1 = "?t="
    p2 = "&p=%"

    par1, par2, opt = photo_mode() #MOVING TO PHOTO MODE
    urllib2.urlopen(df + par1 + "/" + par2 + p1 + passwd + p2 + opt)
    time.sleep(1)

    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Taking a pic")
    par1, par2, opt = shut()  #TAKE A PIC
    urllib2.urlopen(df + par1 + "/" + par2 + p1 + passwd + p2 + opt)
    time.sleep(2)

    url = "http://10.5.5.9:8080/gp/gpMediaList" #FIND THE PICTURE USING SOME REGEX
    content = urllib2.urlopen(url).read()
    content = str(content)
    folder=""
    lastfile=""
    parsed_resp = json.loads(content)
    for key in parsed_resp['media']:
        folder=key['d']
    for key in parsed_resp['media']:
        for key2 in key['fs']:
            lastfile=key2['n']
    time.sleep(1)
    print("\n\r[" + extra.colors.yellow + ".." + extra.colors.end + "] Downloading the pic")
    dow = "http://10.5.5.9:8080/videos/DCIM/" + folder +"/" + lastfile #DOWNLOAD THE PIC AND SAVE IT TO output/
    getFoto = urllib.URLopener()
    getFoto.retrieve("http://10.5.5.9:8080/videos/DCIM/" + folder +"/" + lastfile, "outputs/" + lastfile)
    print("\r\n[" + extra.colors.green + "+" + extra.colors.end + "] Picture saved in outputs/"+lastfile+"\r\n")
    try :
        time.sleep(2)
        process = subprocess.Popen("eog -f outputs/"+lastfile, shell=True, stdout=subprocess.PIPE)
    except :
        pass

#TODO : ADD INFO() FUNCTION TO GET ALL INFORMATIONS ABOUT THE GOPRO AND ADD DELALL() THAT DELETE ALL FILES ON GOPRO
