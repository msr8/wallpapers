import pyperclip as cp
import os

curr_dir = os.path.dirname(__file__)
wp_dir   = curr_dir
md_fp    = os.path.join(curr_dir, 'README.md')

lst = []

for i in sorted(os.listdir(wp_dir)):
    fn,ext = os.path.splitext(i)
    ext = ext.lstrip('.')

    if not ext in ['jpg', 'png', 'jpeg']:    continue   
    if i.startswith('.'):    continue

    path = fn.replace(' ','%20') + '.' + ext
    lst.append((fn,path))


text  = '|     |     |\n'
text += '| :-: | :-: |\n'

while lst:
    a = lst.pop(0)
    b = None if not lst else lst.pop(0)
    
    if a and b:
        images = f'| ![{a[0]}]({a[1]}) | ![{b[0]}]({b[1]}) |\n'
        names  = f'| {a[0]} | {b[0]} |\n'
    else:
        images = f'| ![{a[0]}]({a[1]}) |  |\n'
        names  = f'| {a[0]} |  |\n'
    
    text += names + images


with open(md_fp,'w') as f:
    f.write(text)









