import PySimpleGUI as sg
import speedtest


sg.theme('DarkBlue2')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Check Your Internet Speed')],
            [sg.Button('CHECK'), sg.Button('Exit')] ]

# Create the Window
window = sg.Window('INTERNET SPEED TEST', layout,size=(300, 90))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in  (None, 'Exit'):
        break # if user closes window or clicks Exit
        break
    if event == 'CHECK': # if user clicks CHECK
        wifi  = speedtest.Speedtest()
        def bytes_to_mb(bytes): # convert bytes to MB
            KB = 1024 # One Kilobyte is 1024 bytes
            MB = KB * 1024 # One MB is 1024 KB
            return int(bytes/MB)
        download_speed = bytes_to_mb(wifi.download())
        upload_speed = bytes_to_mb(wifi.upload())
        sg.Popup("Download :", download_speed,"MB"," \nUpload :",upload_speed,"MB")


window.close()