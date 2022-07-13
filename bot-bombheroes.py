import pyautogui, keyboard, time

cat = """




                  ,--.!,
               __/   -*-
             ,d08b.  '|`
             0088MM     
             `9MMP'     
          BOT BOMB HEROES      

>>---> Pressione Q para parar o bot.
"""


print(cat)
time.sleep(2)

def Release():
	while True:
		try:
			pyautogui.click('hero.PNG',duration=2)
			time.sleep(4)
		except:
			if keyboard.is_pressed('q'):
				print("Finalizado Com Sucesso\n")
				break

Release()