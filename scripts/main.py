#!/usr/bin/env python
import urllib2, threading, extra, commands, time, os, subprocess
from subprocess import call

def main(): ##MAIN FUNCTION
    extra.logo()
    call(["clear"])
    passwd = check()
    kc = threading.Thread(target=keepConn)
    kc.start()
    print("["+extra.colors.cyan+"*"+extra.colors.end+"] To see available commands use \"help\"\r\n")
    while True:
        command = raw_input(extra.colors.cyan+"#"+extra.colors.green+"GoPro "+extra.colors.end+"> "+extra.colors.end)
        command = command.strip("")
        launch(command, passwd)

def launch(command, passwd):
    df = "http://10.5.5.9/" #DEFINING THE DEFAULT PARTS
    p1 = "?t="
    p2 = "&p=%"

    # DEFINING COMMANDS
    valid = True

    if command == "on":
        par1, par2, opt = commands.on()
    elif command == "off":
        par1, par2, opt = commands.off()
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
        commands.exit()
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
        try :
            urllib2.urlopen(df+par1+"/"+par2+p1+passwd+p2+opt)
            time.sleep(0.5)
            print("\r\n["+extra.colors.green+"+"+extra.colors.end+"] Command executed successfully ;)\r\n")
        except :
            print("\r\n["+extra.colors.red+"-"+extra.colors.end+"] Error launching the command\r\n")

def connLost():  #IF THE CONNECTION IS LOST
    print("\r\n\r\n[" + extra.colors.red + "-" + extra.colors.end + "] Connection error!\r\n")
    os._exit(1)

def keepConn():  #CHECK IF THE CONNETION IS STABLE
    st = 0
    while True:
        kl = subprocess.call("ping -c 1 10.5.5.9", shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
        if kl == 0:
            time.sleep(5)
            continue
        else:
            st += 1
        if st == 2 :
            connLost()
        else:
            continue

def timer():  #A TIMER
    global p
    secs = 0
    while secs != 7 and p == False:
        time.sleep(1)
        secs += 1
    if p == False:
        raise notConnected()

def check():  #CONNECT TO THE GOPRO
    f = open("passwd.txt", "r")
    pas = str(f.read()).strip("\n") #LOAD THE PASSWORD
    f.close()
    while True:
        if pas != "":  #SEE IF THE USER WANTS TO USE HIS OLD PASSWORD OF IF HE WANTS TO CHANGE IT
            use = str(raw_input("["+extra.colors.cyan+"*"+extra.colors.end+"] Found a password from logs: "+extra.colors.yellow+pas+extra.colors.end+". Use this password? [Y/N] : "))
            if use == "Y" or use== "y":
                break
            elif use == "N" or use == "n":
                pas = str(raw_input("\r\n[" + extra.colors.cyan + "*" + extra.colors.end + "] Enter the password to connect to your GoPro : "))
                f = open("passwd.txt", "w")
                f.write(pas)
                f.close()
                break
            else:
                continue
        else:  #IF THERE'S NO PASSWORD CREATE A NEW ONE
            pas = str(raw_input("[" + extra.colors.cyan + "*" + extra.colors.end + "] Enter the password to connect to your GoPro : "))
            f = open("passwd.txt", "w")
            f.write(pas)
            f.close()
            break
    print("\r\n["+extra.colors.yellow+".."+extra.colors.end+"] Checking if you are connected to a GoPro")
    try: #TRY TO CONNECT TO THE GOPRO
        global p
        p = False
        tm = threading.Thread(target=timer) #START THE TIME
        tm.start()
        urllib2.urlopen("http://10.5.5.9/bacpac/PW?t=" + pas + "&p=%01")
        p = True
        tm.join()
        print("\r\n["+extra.colors.green+"+"+extra.colors.end+"] Yay, you are now connected to your GoPro. Dropping the shell...\r\n")
        time.sleep(0.5)
        return(pas)
    except urllib2.HTTPError: #IF CONNECTION IS FAILED
        notConnected()
    except :
        notConnected()

def notConnected(): #THE GOPRO ISN'T CONNECTED
    print("\r\n[" + extra.colors.red + "-" + extra.colors.end + "] Check your connection or your password for the GoPro and come back!\r\n")
    os._exit(1)

if __name__=="__main__":  #LAUNCH THE PROGRAM
    try:
        main()
    except KeyboardInterrupt :  #KEYBOARD INTERRUPTION PREVENTION
        print("\r\n["+extra.colors.red+"-"+extra.colors.end+"] Quitting ...\r\n")
        time.sleep(1)
        call(["clear"])
        os._exit(1)
