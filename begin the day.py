import os
import time
import webbrowser



mode = 0

print("This program started on "+time.ctime())
while(mode!=4):
    mode = int(input("What's the mode? \n1-site1/site2/site3/site4/site5\n2-site6/site7/site8/site9/site10\n3-mode3\n4-close\n"))
    if(mode == 1):
        webbrowser.open("Coloque a URL do seu site aqui")
        webbrowser.open("Coloque a URL do seu site aqui")
        webbrowser.open("Coloque a URL do seu site aqui")
        webbrowser.open("Coloque a URL do seu site aqui")
        webbrowser.open("Coloque a URL do seu site aqui")
    
    if(mode == 2):
        os.startfile('chrome')
        webbrowser.open("Coloque a URL do seu site aqui",new = 1)
        webbrowser.open_new_tab("Coloque a URL do seu site aqui")
        webbrowser.open_new_tab("Coloque a URL do seu site aqui")
        webbrowser.open_new_tab("Coloque a URL do seu site aqui")
        webbrowser.open_new_tab("Coloque a URL do seu site aqui")
        webbrowser.open_new_tab("Coloque a URL do seu site aqui")
    if(mode == 3):
        os.startfile('chrome')
        webbrowser.open("Coloque a URL do seu site aqui")
        webbrowser.open("Coloque a URL do seu site aqui")
        webbrowser.open("Coloque a URL do seu site aqui")
        webbrowser.open("Coloque a URL do seu site aqui")
