import pyperclip as cp
import os

curr_dir = os.path.dirname(__file__)
wp_dir = curr_dir

text = '''# Wallpaper Preview\n\n<br>\n\n'''

for i in sorted(os.listdir(wp_dir)):
    ext = os.path.splitext(i)[1]
    if not ext in ['.jpg', '.png', '.jpeg']:    continue   

    if i.startswith('.'):    continue

    i2 = i.replace(' ','%20')
    text += f'''## {i}
<details>\n
![{i}](./{i2})\n
</details>\n\n'''

# print(text)
# cp.copy(text)
# print('Copied to clipboard!')

with open('README.md', 'w') as f:
    f.write(text)

print('Written to README.md!')






