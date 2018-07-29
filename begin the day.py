import os
import time
import webbrowser



mode = 0

print("This program started on "+time.ctime())
while(mode!=4):
    mode = int(input("What's the mode? \n1-Gmail/smartx/keep/Unum/PulsWiki\n2-Trix/Jira/ConfigFelipe/FemsaMínimo/Puls\n3-mode3\n4-close\n"))
    if(mode == 1):
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        webbrowser.open("https://smartx.trixlog.com/#/control_panel")
        webbrowser.open("https://keep.google.com/u/0/")
        webbrowser.open("http://10.10.2.201:8080/sistema/trixlog/-1898188217")
        webbrowser.open("https://puls.calamp.com/wiki/PULS_API")
    
    if(mode == 2):
        os.startfile('chrome')
        webbrowser.open("http://acesso.trixlog.com/",new = 1)
        webbrowser.open_new_tab("https://jira.trixlog.com/issues/?jql=project%20%3D%20CONFIGURAR%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20key%20ASC%2C%20priority%20DESC%2C%20updated%20DESC")
        webbrowser.open_new_tab("https://docs.google.com/spreadsheets/d/1R5kBoiv7l5msWh58WKMTARKbzRnsMMapRObggELYxGI/edit#gid=1042056563")
        webbrowser.open_new_tab("https://docs.google.com/spreadsheets/d/1dhBUk83FVg8TCe3VWyMMwUlZp1cVQROW0pk8E2gl6Gw/edit#gid=0")
        webbrowser.open_new_tab("https://puls.calamp.com/devicemgr/devices.php")
        webbrowser.open_new_tab("https://docs.google.com/spreadsheets/d/1_2Ay7MZMN3dfDyR-IfVn_xJL7Ql6v3TkuqIpLKxTjH0/edit?ts=5b294101#gid=93073105")
    if(mode == 3):
        webbrowser.open("")
        webbrowser.open("")
        webbrowser.open("")
        webbrowser.open("")
