import pyttsx3

engine = pyttsx3.init(driverName="sapi5")

# -------- Modify speaking rate --------- #
# print(engine.getProperty('rate'))
engine.setProperty('rate', 350)

# -------- Modify volume ------------ #
# print(engine.getProperty('volume'))

# -------- Make engine talk ---------- #
sayThis = "Hello. I'm a computer generated voice. It took Jack 90 minutes or so to get me to say this sentence. This" \
          "sure is harder than it looks! Still, I'm sure he will learn."
engine.say(sayThis)
engine.runAndWait()
