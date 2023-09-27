import os
from datetime import date

today = date.today()
formatted = today.strftime("%d/%m/%Y")
commitName = 'git commit -m \"%s\"'%formatted

print('Generating Portuguese OTS pack exclusives', flush=True)
os.system('python3.11 pt.py')
print('Generating the actual banlist', flush=True)
os.system('python3.11 lflistgen.py')
print('Generating cc++ banlist', flush=True)
os.system('git add .')
os.system(commitName)
os.system('git push')