
import sys

for i in range(5):
    for j in range(i+1):
        sys.stdout.write("*")
    print()

print()
for i in range(1, 6):
    print("*" * i)

print()
print("\n".join("*" * i for i in range(1, 6)))
