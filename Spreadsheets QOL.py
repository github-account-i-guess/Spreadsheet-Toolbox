import pygame,time,pyautogui,os,sys
width = 500
height = 350
lines = 0
clock=pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
def path(file_in):
    fileDir = os.path.abspath(__file__)
    parentDir = os.path.dirname(fileDir) 
    return os.path.join(parentDir, file_in)
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    pyautogui.hotkey('alt','tab')
                    lines= 0
                    e = path('options.txt')
                    f =open(e,'r')
                    f_r = (f.readlines())
                    f_r_2 = []
                    for i in f_r:
                        i = i.strip('\n')
                        f_r_2.append(i)
                    f_r = f_r_2
                    if f_r[2] == 'Pie' and f_r[8] == 'True':
                        if f_r[4] >f_r[6]:
                            larger_line = int(f_r[4])
                        else:
                            larger_line = int(f_r[6])
                        pyautogui.hotkey('up')
                        print (larger_line)
                        for i in range(larger_line):
                            lines += 1
                            pyautogui.hotkey('ctrl','c')
                            pyautogui.hotkey('backspace')
                            for i in range(lines):
                                pyautogui.hotkey('left')
                            pyautogui.hotkey('ctrl','v')
                            for i in range(lines):
                                pyautogui.hotkey('down')
                            pyautogui.hotkey('ctrl','c')
                            pyautogui.hotkey('backspace')
                            for i in range(lines):
                                pyautogui.hotkey('up')
                                pyautogui.hotkey('right')
                            pyautogui.hotkey('ctrl','v')
                            for i in range(lines):
                                pyautogui.hotkey('left')
                            pyautogui.hotkey('ctrl','c')
                            pyautogui.hotkey('backspace')
                            for i in range(lines):
                                pyautogui.hotkey('down')
                            pyautogui.hotkey('ctrl','v')
                            for i in range(lines):
                                pyautogui.hotkey('up')
                                pyautogui.hotkey('right')
                            pyautogui.hotkey('right')
                        for i in range(larger_line):
                            pyautogui.hotkey('left')
                        pyautogui.hotkey('down')
                        lines = 0
                    if  f_r[2]== 'Pie' and f_r[6] == '1':
                        lines =1
                        amount = int(f_r[4])
                        for i in range(amount):
                            for i in range(amount-lines):
                                pyautogui.hotkey('right')
                                time.sleep(0.05)
                            pyautogui.hotkey('ctrl','c')
                            pyautogui.hotkey('backspace')
                            for i in range(amount-lines):
                                pyautogui.hotkey('left')
                                time.sleep(0.05)
                            for i in range(amount-lines):
                                pyautogui.hotkey('down')
                                time.sleep(0.05)
                            pyautogui.hotkey('ctrl','v')
                            for i in range(amount-lines):
                                pyautogui.hotkey('up')
                                time.sleep(0.05)
                            lines += 1
                    elif f_r[2]== 'Pie' and int(f_r[6]) > 1:
                        lines = 1
                        lines2 = 0
                        amount = int(f_r[4])
                        amount2 = int(f_r[6])
                        pyautogui.hotkey('down')
                        if True:
                            pyautogui.hotkey('ctrl','c')
                            for z in range(amount-1):
                                pyautogui.hotkey('down')
                            pyautogui.hotkey('ctrl','v')
                            for z in range(amount):
                                pyautogui.hotkey('up')
                            pyautogui.hotkey('down')
                        for i in range(amount2-1)[1:]:
                            print (i)
                            pyautogui.hotkey('down')
                            pyautogui.hotkey('ctrl','c')
                            for z in range((i+1)*amount-i-1):
                                pyautogui.hotkey('down')
                            pyautogui.hotkey('ctrl','v')
                            for z in range((i+1)*amount-i-1):
                                pyautogui.hotkey('up')
                        for i in range(amount2-1):
                            pyautogui.hotkey('up')
                        for i in range(amount):
                            for i in range(amount-lines):
                                pyautogui.hotkey('right')
                                time.sleep(0.05)
                            pyautogui.hotkey('ctrl','c')
                            pyautogui.hotkey('backspace')
                            for i in range(amount-lines):
                                pyautogui.hotkey('left')
                                time.sleep(0.05)
                            for i in range(amount-lines):
                                pyautogui.hotkey('down')
                                time.sleep(0.05)
                            pyautogui.hotkey('ctrl','v')
                            for i in range(amount-lines):
                                pyautogui.hotkey('up')
                                time.sleep(0.05)
                            lines+=1
                            lines2+=1
                        pyautogui.hotkey('down')
                        lines2 -=1
                        for i in range(amount2-1):
                            lines = 1
                            for i in range(amount-1):
                                for i in range(amount-lines):
                                    pyautogui.hotkey('right')
                                    time.sleep(0.05)
                                pyautogui.hotkey('ctrl','c')
                                pyautogui.hotkey('backspace')
                                for i in range(amount-lines):
                                    pyautogui.hotkey('left')
                                    time.sleep(0.05)
                                for i in range(amount-lines):
                                    pyautogui.hotkey('down')
                                    time.sleep(0.05)
                                for i in range(lines2):
                                    pyautogui.hotkey('down')
                                    time.sleep(0.05)
                                pyautogui.hotkey('ctrl','v')
                                for i in range(amount-lines):
                                    pyautogui.hotkey('up')
                                    time.sleep(0.05)
                                for i in range(lines2):
                                    pyautogui.hotkey('up')
                                    time.sleep(0.05)
                                lines+=1
                            lines2 +=amount -1
                            pyautogui.hotkey('down')
                    if  f_r[2]== 'Bar' and f_r[4] == '1':
                        amount = int(f_r[6])-1
                        for i in range(amount):
                            for i in range(amount-lines):
                                pyautogui.hotkey('down')
                                time.sleep(0.05)
                            pyautogui.hotkey('ctrl','c')
                            pyautogui.hotkey('backspace')
                            for i in range(amount-lines):
                                pyautogui.hotkey('up')
                                time.sleep(0.05)
                            for i in range(amount-lines):
                                pyautogui.hotkey('right')
                                time.sleep(0.05)
                            pyautogui.hotkey('ctrl','v')
                            for i in range(amount-lines):
                                pyautogui.hotkey('left')
                                time.sleep(0.05)
                            lines += 1
                    elif  f_r[2]== 'Bar' and int(f_r[4]) > 1:
                        amount = int(f_r[6])-1
                        for i in range(amount):
                            for i in range(amount-lines):
                                pyautogui.hotkey('down')
                            pyautogui.hotkey('ctrl','c')
                            pyautogui.hotkey('backspace')
                            for i in range(amount-lines):
                                pyautogui.hotkey('up')
                            for i in range(amount-lines):
                                pyautogui.hotkey('right')
                            pyautogui.hotkey('ctrl','v')
                            for i in range(amount-lines):
                                pyautogui.hotkey('left')
                            lines += 1
                    f.close()
                if event.key == pygame.K_c:
                    pyautogui.hotkey('alt','tab')
                    pyautogui.hotkey('ctrl','f')
                    for i in range(10):
                        pyautogui.hotkey('backspace')
                        pyautogui.hotkey(str(i))
                        p= pyautogui.locateCenterOnScreen(path('Find Selection.jpg'))
                        if not p == None:
                            time.sleep(0.1)
                            pyautogui.click(p)
                            pyautogui.hotkey('backspace')
                            pyautogui.hotkey(str(i))
                            pyautogui.hotkey('enter')
                            pyautogui.hotkey('ctrl','f')
                    