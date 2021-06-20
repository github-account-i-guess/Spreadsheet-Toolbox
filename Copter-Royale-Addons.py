import pyautogui, time,pygame,PIL,sys,random

from pygame.constants import K_r
pygame.init
width = 500
height = 350
clock=pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
ab = False
ab_time = 0
rs = False
rs_time = 0
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    pyautogui.click(1572,45)
                    for i in range(5):
                        time.sleep(0.2)
                        pyautogui.hotkey('ctrl','t')
                        pyautogui.typewrite('https://www.coolmathgames.com/0-copter-royale')
                        pyautogui.press('enter')
                    time.sleep(17)
                    pyautogui.click(1339,1069)
                    print('done')
                if event.key == pygame.K_c:
                    for i in range(5):
                        time.sleep(0.2)
                        pyautogui.hotkey('ctrl','tab')
                        pyautogui.click(1915,325)
                        pyautogui.scroll(-1100)
                        pyautogui.click(1060,300)
                if event.key == pygame.K_u:
                    for i in range(5):
                        time.sleep(0.2)
                        pyautogui.hotkey('ctrl','tab')
                        pyautogui.click(1915,325)
                        pyautogui.scroll(1100)
                if event.key == pygame.K_p:
                    for i in range(5):
                        time.sleep(0.5)
                        pyautogui.hotkey('ctrl','tab')
                        pyautogui.click(1915,325,1,0,'left')
                        pyautogui.scroll(-500)
                        pyautogui.click(740,770)
                if event.key == pygame.K_x:
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()  
                        for i in range(5):
                            pyautogui.hotkey('ctrl','tab')
                            pyautogui.click(1915,325)
                            pyautogui.hotkey('pageup')
                            pyautogui.scroll(-375)
                            pyautogui.click(905,780,2,1,'left')
                            pyautogui.click(890,435,1,0,'left')
                            pyautogui.click(778, 752,1,1,'left')
                            pyautogui.click(890,435,1,0,'left')
                            pyautogui.click(905,780,1,0,'left')
                        e=0
                        for i in range(300):
                            time.sleep(0.1)
                            e+= 0.1
                            print (e)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit() 
                                if event.type == pygame.KEYDOWN:
                                    if event.key ==pygame.K_b:
                                        break
                if event.key == pygame.K_b:
                    ab = not ab
                    pyautogui.hotkey('alt','tab')
                if event.key == pygame.K_r:
                    rs = not rs
                    f = pyautogui.position()
                    pyautogui.hotkey('alt','tab')

    if ab:
        pyautogui.rightClick()
        ab_time += 1
    if rs:
        pyautogui.moveTo(f)
        pyautogui.move(random.randint(-10,10),random.randint(-10,10))
        pyautogui.leftClick()
        rs_time += 1
    if rs_time > 5:
        rs = False
        rs_time = 0
        pyautogui.hotkey('alt','tab')
    if ab_time > 200:
        ab = False
        ab_time = 0
        pyautogui.hotkey('alt','tab')
#copter-royale-qol-addons
