import speech_recognition as sr
 
r = sr.Recognizer()
m = sr.Microphone()
 
try:
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        try:
            value = r.recognize_google(audio, language="vi-VN")
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(format(value).encode("utf-8"))
            # else: # this version of Python uses unicode for strings (Python 3+)
                # print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError:
            print("Uh oh! Couldn't request results from Google Speech Recognition service")
except KeyboardInterrupt:
    pass
