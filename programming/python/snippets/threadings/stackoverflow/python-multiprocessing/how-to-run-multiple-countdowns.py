from threading import Timer

def spong(what):
    print(what)



threads = {4.0: "four point ho",
            6.0: "six point oh",
            2.0: "two point oh"
        }

for key, val in threads.items():
    Timer(key, spong, args=(val,)).start()

print("And, they're off!")


#https://stackoverflow.com/questions/71257921/how-to-run-multiple-countdowns