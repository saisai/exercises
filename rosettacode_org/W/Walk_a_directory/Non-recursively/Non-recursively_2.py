
import os
for filename in os.listdir("."):
    if filename.endswith(".py"):
        print(filename)
