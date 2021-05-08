from subprocess import call

def say(word):
    print(word,end=" ")
    call(['wsay.exe',word])

say("eloise")