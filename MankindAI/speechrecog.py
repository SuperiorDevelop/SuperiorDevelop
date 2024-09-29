import speech_recognition as sr
# import pyaudio
import os
import threading
from mtranslate import translate
from colorama import Fore,Style,init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.Green + "Listening...", end = "", flush=True)
        print(Style.RESET_ALL, end="", flush=True)
        
def hin_to_eng(text):
    eng_text = translate(text, "en-us")
    return eng_text
    
def speech_to_text():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2
    
    with sr.Microphone() as src:
        recognizer.adjust_for_ambient_noise(src)
        while True:
            print(Fore.GREEN + "Listening...", end="", flush=True)
            try:
                audio = recognizer.listen(src)
                print("\r" + Fore.LIGHTBLACK_EX + "Recognizing...", end="", flush=True)
                recognizer_text = recognizer.recognize_google(audio).lower()
                if recognizer_text:
                    trans_text = hin_to_eng(recognizer_text)
                    print("\r" + Fore.BLUE + "Superior: " + trans_text)
                    return trans_text
                else:
                    return ""
                
            except sr.UnknownValueError:
                recognizer_text = ""
            finally:
                print("\r", end="", flush=True)
            
            os.system("cls" if os.name == "nt" else "clear")
            
        stt_thread = threading.Thread(target = speech_to_text)
        print_thread = threading.Thread(target = print_loop)
        stt.thread.start()
        print_lool.start()
        stt_thread.join()
        print_loop.join()
        
speech_to_text()        