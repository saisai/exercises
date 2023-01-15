import io

# writing to a buffer
output = io.StringIO()
output.write("This goes into the buffer. ")
print("And so does this.", file=output)

# retrieve the value written
print(output.getvalue())

output.close() #  discard buffer memory

# initialize a read buffer
inpt = io.StringIO("Initial value for the read buffer")

# read from the buffer
print(inpt.read())