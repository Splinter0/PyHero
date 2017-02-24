#!/usr/bin/env python

"""IMPORTING ALL THE STUFF WE NEED"""

import threading, extra, commands, time, os, subprocess, urllib2, re, json, cms
from wol import *


heroIp = "10.5.5.9"

def main(): ##MAIN FUNCTION

    """MAIN FUNCTION"""

    extra.logo()
    subprocess.call(["clear"])
    passwd, camera = connect()
    print("["+extra.colors.cyan+"*"+extra.colors.end+"] To see available commands use \"help\"\r\n")
    while True:
        command = raw_input(extra.colors.cyan+"#"+extra.colors.green+"GoPro "+extra.colors.end+"> "+extra.colors.end)
        command = command.strip("")
        launch(command, passwd, camera)

def launch(command, passwd, camera):

    """THIS FUNCTION MANAGE THE COMMANDS TO LAUNCH """

    if passwd :
        df = "http://"+heroIp+"/"  # DEFINING THE DEFAULT PARTS FOR GOPRO 2/3/3+
        p1 = "?t="
        p2 = "&p=%"
    else :
        pass

    # DEFINING COMMANDS
    valid = True

    if command == "on":
        par1, par2, opt = commands.on(passwd, camera)
        if not passwd and camera != "HERO4 Session":  #IF IT ISN'T A HERO2/3/3+ OR HERO4 Session we need to use a different command
            valid = False
    elif command == "off":
        par1, par2, opt = commands.off(passwd, camera)
    elif command == "shoot":
        par1, par2, opt = commands.shut()
    elif command == "stop_rec":
        par1, par2, opt = commands.stop()
    elif command == "no_leds":
        par1, par2, opt = commands.no_leds()
    elif command == "preview_on":
        par1, par2, opt = commands.prev_on()
    elif command == "preview_off":
        par1, par2, opt = commands.prev_off()
    elif command == "video":
        par1, par2, opt = commands.video_mode()
    elif command == "photo":
        par1, par2, opt = commands.photo_mode()
    elif command == "brust":
        par1, par2, opt = commands.brust_mode()
    elif command == "timelapse":
        par1, par2, opt = commands.timelapse_mode()
    elif command == "timer":
        par1, par2, opt = commands.timer_mode()
    elif command == "play_hdmi":
        par1, par2, opt = commands.play_hdmi()
    elif command == "orientation_up":
        par1, par2, opt = commands.or_up()
    elif command == "orientation_down":
        par1, par2, opt = commands.or_down()
    elif command == "fov_wide":
        par1, par2, opt = commands.fov_wide()
    elif command == "fov_medium":
        par1, par2, opt = commands.fov_med()
    elif command == "fov_narrow":
        par1, par2, opt = commands.fov_nar()
    elif command == "mute":
        par1, par2, opt = commands.no_vol()
    elif command == "volume_70":
        par1, par2, opt = commands.vol_70()
    elif command == "volume_100":
        par1, par2, opt = commands.vol_100()
    elif command == "protune_on":
        par1, par2, opt = commands.pro_on()
    elif command == "protune_off":
        par1, par2, opt = commands.pro_off()
    elif command == "2_leds":
        par1, par2, opt = commands.leds2()
    elif command == "4_leds":
        par1, par2, opt = commands.leds4()
    elif command.startswith("autopoweroff"):
        command = command.strip("autopoweroff ")
        if command == "nev":
            par1, par2, opt = commands.autoN()
        elif command == "60s":
            par1, par2, opt = commands.auto60()
        elif command == "120s":
            par1, par2, opt = commands.auto120()
        elif command == "300s":
            par1, par2, opt = commands.auto300()
        else :
            print("\r\n["+extra.colors.red+"-"+extra.colors.end+"] Use : autopoweroff \"option\" (run \"help\" to see the options)\r\n")
            valid = False
    elif command == "shoot&get":
        commands.getLast(passwd)
        valid = False
    elif command == "stealth_mode":
        commands.stealth_mode(passwd)
        valid = False
    elif command == "stealth_mode_off":
        commands.stealth_off(passwd)
        valid = False
    elif command == "exit":
        commands.bye()
        valid = False
    elif command == "help":
        commands.help()
        valid = False
    elif command == "":
        valid = False
    else :
        print("\r\n["+extra.colors.red+"-"+extra.colors.end+"] Wrong command\r\n")
        valid = False
    if valid == True: ##LAUNCH THE COMMAND
        if passwd :  ##THIS IS FOR GOPRO2/3/3+
            try :
                global close
                close = False
                tm = threading.Thread(target=timer)
                tm.start()   ## START THE TIMER
                urllib2.urlopen(df+par1+"/"+par2+p1+passwd+p2+opt)
                close = True
                time.sleep(0.5)
                print("\r\n["+extra.colors.green+"+"+extra.colors.end+"] Command executed successfully ;)\r\n")
            except :
                print("\r\n["+extra.colors.red+"-"+extra.colors.end+"] Error launching the command\r\n")
                cc = threading.Thread(target=checkConn)
                cc.start()
        else :
            try :  #AND THIS FOR ALL THE OTHERS
                global close
                close = False
                tm = threading.Thread(target=timer)
                tm.start()   ## START THE TIMER
                urllib2.urlopen(par1)
                close = True
                time.sleep(0.5)
                print("\r\n["+extra.colors.green+"+"+extra.colors.end+"] Command executed successfully ;)\r\n")
            except :
                print("\r\n["+extra.colors.red+"-"+extra.colors.end+"] Error launching the command\r\n")
                cc = threading.Thread(target=checkConn)
                cc.start()

def connect():

    """THIS FUNCTION :
        -FIRST CHECKS IF YOU ARE ACTUALLY CONNECTED TO A GOPRO
        -SECOND LAUNCHES THE detect() FUNCTION TO FIND WHAT TYPE OF GOPRO YOU'RE USING
        -THIRD IF THE CAMERA IS AN HERO3/3+/2 MEANS THAT IT NEEDS A PASSWORD OTHERWISE CHECK IF THE CAMERA
            IS A GOPRO4 Session AND IF IT IS THE PROGRAM HAS TO LAUNCH THE wake() FUNCTION IN ORDER TO INTERACT WITH IT"""

    print("[" + extra.colors.yellow + ".." + extra.colors.end + "] Checking if you are connected to a GoPro")
    time.sleep(0.5)
    conn = subprocess.call("ping -c 1 "+heroIp, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
    if conn == 0:
        print("\r\n[" + extra.colors.cyan + "*" + extra.colors.end + "] You are connected to a GoPro\r\n")
        camera, passReq = detect()
        if passReq == True:
            pass
        else :
            global mac
            mac = getMac()
            if camera == "HERO4 Session":
                wake(camera)
            else : pass
            print("\r\n[" + extra.colors.green + "+" + extra.colors.end + "] Dropping the shell...\r\n")
            return(passReq, camera)
        while True :
            print("[" + extra.colors.yellow + ".." + extra.colors.end + "] Gathering the password")
            time.sleep(0.5)
            try :
                passwd = urllib2.urlopen("http://10.5.5.9/bacpac/sd").read()
                passwd = str(passwd.encode("utf-8"))
                passwd = re.sub(r'\W+', '', passwd)
                print("\r\n[" + extra.colors.green + "+" + extra.colors.end + "] Yay, you are now connected to your GoPro. Dropping the shell...\r\n")
                return(passwd, camera)
            except :
                print("\r\n[" + extra.colors.red + "-" + extra.colors.end + "] An error incurred while trying to get the password\r\n")
                again = str(raw_input("[" + extra.colors.cyan + "*" + extra.colors.end + "] Do you want to try again? [Y/N] : "))
                if again == "Y" or again== "y":
                    subprocess.call(["clear"])
                    continue
                elif again == "N" or again == "n":
                    print("\r\n[" + extra.colors.cyan + "*" + extra.colors.end + "] Bye ;)")
                    time.sleep(1)
                    subprocess.call(["clear"])
                    os._exit(1)
                    break
    else :
        notConnected()


def detect():

    """THIS FUNCTION USE A DICTIONARY OF GOPRO'S CODE-NAME TO FIND WHAT TYPE OF GOPRO YOU'RE USING"""

    print("[" + extra.colors.yellow + ".." + extra.colors.end + "] Detecting your GoPro model")
    cameras = cms.cameras
    found = False
    try:
        response = urllib2.urlopen('http://10.5.5.9/gp/gpControl/info').read()
        for key, camera in cameras.iteritems():  ##CHECKS FOR EVERY CAMERA IN THE DICTIONARY
            if camera in response:  # IF IT IS IN THE RESPONSE
                finalCam = key  # CREATE A VARIABLE WITH THE KEY OF THE CAMERA (THE ACTUAL CAMERA'S NAME)
                found = True
                passReq = False
            else:
                raise
    except:
        response = urllib2.urlopen('http://10.5.5.9/camera/cv').read()  # SO THEN CREATE A NEW RESPONSE
        for x in range(5):  # CHECKS ONLY FOR THE FIRST 6 CAMERAS
            for key, camera in cameras.iteritems():
                if camera in response:
                    finalCam = key
                    found = True
                    passReq = True
                else:
                    pass

        if found == False:
            cameraNotFound()
        else :
            pass
    finally :
        print("\r\n[" + extra.colors.green + "+" + extra.colors.end + "] It is a GoPro "+finalCam+"\r\n")
        return(finalCam, passReq)

def getMac():

    """THIS FUNCTION IS USED TO GET THE MAC ADDRESS OF THE CAMERA, WE NEED IT BECAUSE SOME CAMERAS WANT A WOL PACKET
        TO TURN ON AND IN ORDER TO FORGE ONE OF IT WE FIRST NEED THE MAC ADDRESS"""

    cmd = "arp -a"  # command to get the GoPro's MAC address
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, errors = p.communicate()
    if output is not None:  # format the output better
        for i in output.split("\n"):
            if heroIp in i:
                for mac in i.split():
                    if ":" in mac:
                        return (mac)

    else:
        print("\r\n[" + extra.colors.red + "-" + extra.colors.end + "] Fatal error trying to grab the MAC of your camera!\r\n")
        raw_input("")
        commands.bye()

def wake(camera):

    """THIS FUNCTION USES Wake On Lan PACKET FOR HERO+/+ LCD/4/4 Session"""

    try :
        send_magic_packet(mac, ip_address=heroIp, port=9)
        time.sleep(2)
        if camera == "HERO4 Session":  #HERO4 Session needs to be monitored if it gets the command
            checkUrl = "http://10.5.5.9/gp/gpControl/status"
            status = urllib2.urlopen(checkUrl).read()
            status = str(status)
            content = json.loads(status)
            content = content(["status"]["32"])
            if content != "0":
                pass
            else :
                raise ValueError("Your camera did not allow the program to connect")

    except Exception as e:
        print("["+extra.colors.red +"-"+extra.colors.end+"] Check your connection with the GoPro... If you think the connectio is ok this is the error:\r\n"+e+"\r\n")
        print(extra.colors.red + "Report this error at : " + extra.colors.cyan + "https://github.com/Splinter0/PyHero/issues" + extra.colors.end + "\r\n")
        raw_input("")
        commands.bye()



### SUPPORT FUNCTIONS ###


def connLost():  #IF THE CONNECTION IS LOST
    print("\r\n[" + extra.colors.red + "-" + extra.colors.end + "] Connection error! Check your connection with the GoPro\r\n")
    os._exit(1)

def checkConn():  #CHECK IF THE CONNETION IS STABLE

    """THIS FUNCTION IS USED TO CHECK IF THE CONNECTION IS STILL ALIVE
        IT IS CALLED BY THE LAUNCH FUNCTION WHEN A COMMAND FAILS TO CHECK
        IF THE CONNECTION IS STILL ALIVE INSTEAD OF DIRECTLY INTERRUPT THE PROGRAM.
        IT ALSO CALLED WHEN THE COMMAND TAKES AN UNEXPECTED TIME TO RESPOND"""

    while True:
        kl = subprocess.call("ping -c 1 10.5.5.9", shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
        if kl == 0: break
        else: connLost()

def timer():  #A TIMER

    """THIS TIME IS USED TO CHECK IF THE COMMAND IS TAKING TOO LONG TO RESPOND (8s)"""

    global close
    secs = 0
    while secs != 8 and close == False:
        time.sleep(1)
        secs += 1
    if close == False:
        raise checkConn()

def notConnected(): #THE GOPRO ISN'T CONNECTED
    print("\r\n[" + extra.colors.red + "-" + extra.colors.end + "] Check your connection with the GoPro and come back!\r\n")
    os._exit(1)

def cameraNotFound():

    """THIS FUNCTION TELLS YOU IF THE GORPO YOU ARE USING IS CURRENTLY SUPPORTED OR NOT BY THE PROGRAM"""

    print("\r\n[" + extra.colors.red + "-" + extra.colors.end + "] Couldn't define your GoPro model, probably it isn't supported. Report it to :\r\n")
    print(extra.colors.cyan +"https://github.com/Splinter0/PyHero/issues"+ extra.colors.end)
    raw_input("")
    commands.bye()

if __name__=="__main__":  #LAUNCH THE PROGRAM
    try:
        main()
    except KeyboardInterrupt :  #KEYBOARD INTERRUPTION PREVENTION
        print("\r\n["+extra.colors.red+"-"+extra.colors.end+"] Quitting ...\r\n")
        time.sleep(1)
        subprocess.call(["clear"])
        os._exit(1)
