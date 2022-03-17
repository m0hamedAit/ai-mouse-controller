
import pyautogui
import speech_recognition as sr 


def listening():
	recognizer = sr.Recognizer()
	print("\n\nThreshold Value Before calibration:" + str(recognizer.energy_threshold))

	while True :
		#speech recognition
		with sr.Microphone() as src:
			try:
				#audio = recognizer.adjust_for_ambient_noise(src)
				print("\nPlease speak:")
				audio = recognizer.listen(src)
				speech_to_txt = recognizer.recognize_google(audio)  #language="fr-FR"
					#speech_to_txt = recognizer.recognize_google_cloud(audio)
			except Exception as ex:
				print("Sorry. Could not understand.\n\n")
				continue
			print("I heard : " + speech_to_txt)
			
			    #---------------------------------------------------------------------
					# The following if-else block is for the commands I have chosen and 
					# call their respective GUI action
					#---------------------------------------------------------------------
			if speech_to_txt in ["quit program","exit program"]:
				break
			elif speech_to_txt in ["left click","click","left-click"] :
				pyautogui.click()
			elif speech_to_txt in ["right click","right-click"]:
				pyautogui.click(button='right')
			elif speech_to_txt in ["double click","double-click"]:
				pyautogui.click(clicks=2)
			elif speech_to_txt in ["scroll up","scroll-up"]:
				pyautogui.scroll(40)   # scroll up 10 "clicks"
			elif speech_to_txt in ["scroll down","scroll-down"]:
				pyautogui.scroll(-40)   # scroll down 10 "clicks"
			elif speech_to_txt in ["scroll left","scroll-left"]:
				pyautogui.hscroll(-10)   # scroll left 10 "clicks"
			elif speech_to_txt in ["scroll right","scroll-right"]:
				pyautogui.hscroll(10)   # scroll right 10 "clicks"
			elif speech_to_txt == "write":
				try:
					audio = recognizer.adjust_for_ambient_noise(src)
					print("\n\nThreshold Value After calibration:" + str(recognizer.energy_threshold))
					print("\nPlease speak:")
					audio = recognizer.listen(src)
					speech_to_txt = recognizer.recognize_google(audio).lower()
							#speech_to_txt = recognizer.recognize_google_cloud(audio)
				except Exception as ex:
					print("Sorry. Could not understand.\n\n")
					continue
				pyautogui.write(speech_to_txt)

if __name__ =="__main__":
	listening()