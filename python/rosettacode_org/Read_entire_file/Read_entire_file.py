
print(open('Read_entire_file.py').read())

print(open('Read_entire_file.py', encoding='utf-8').read())

with open('Read_entire_file.py', encoding='utf-8') as f:
    data = f.read()
    print(data)


from pathlib import Path

any_string = Path('Read_entire_file.py').read_text(encoding='utf-8')
print(any_string)

any_binary_data = Path('Read_entire_file.py').read_bytes()
print(any_binary_data)
