# text_to_audio
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak('how are you')
    speak('kaisea ho danny bhaai')