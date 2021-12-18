# import the necessary packages
import pyautogui
import speech_recognition as sr  #


def listening():
		# The gui instance will be used to call GUI functions defined by us in 'gui_automation.py'
	recognizer = sr.Recognizer()
	print("\n\nThreshold Value Before calibration:" + str(recognizer.energy_threshold))

	##############

	# loop over the frames from the video stream
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
			if (speech_to_txt == "quit program") or (speech_to_txt == "exit program"):
				break
			elif speech_to_txt == "left click" or speech_to_txt == "click" or speech_to_txt == "left-click":
				pyautogui.click()
			elif speech_to_txt == "right click" or speech_to_txt == "right-click":
				pyautogui.click(button='right')
			elif speech_to_txt == "double click" or speech_to_txt == "double-click":
				pyautogui.click(clicks=2)
			elif speech_to_txt == "scroll up" or speech_to_txt == "scroll-up":
				pyautogui.scroll(40)   # scroll up 10 "clicks"
			elif speech_to_txt == "scroll down" or speech_to_txt == "scroll-down":
				pyautogui.scroll(-40)   # scroll down 10 "clicks"
			elif speech_to_txt == "scroll left" or speech_to_txt=="scroll-left":
				pyautogui.hscroll(-10)   # scroll left 10 "clicks"
			elif speech_to_txt == "scroll right" or speech_to_txt=="scroll-right":
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