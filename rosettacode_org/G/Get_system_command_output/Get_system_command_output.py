import subprocess
#returned_text = subprocess.check_output("ls", shell=True, universal_newlines=True)
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print(type(returned_text))
print(returned_text)

