from colorama import Fore, Back, Style
import os
import shutil
BOLD = '\033[1m'
print(Fore.BLUE + "Py-DOS 1.6\nCopyright 2020 ccc814p\n")
home = os.getcwd()
while True:
  cmd = input(BOLD + Fore.GREEN + os.getcwd() + Fore.BLUE + ">" + Fore.WHITE)
  cmd = cmd.split()
  if cmd[0] == 'echo':
    print(' '.join(cmd[1:]))
  if cmd[0] == 'dir':
    print('\n'.join(os.listdir()))
  if cmd[0] == 'del':
    os.remove(cmd[1])
  if cmd[0] == 'open':
    g = open(cmd[1],'r')
    h = g.read()
    print(h)
    g.close()
  if cmd[0] == 'makedir':
    os.mkdir(cmd[1])
  if not cmd[0] in ('start', 'echo', 'dir', 'del', 'open', 'makedir', 'cd', 'ddir', 'help', 'clone', 'rename', 'java', 'move', 'cls', 'python3', 'time', 'date', 'setDate'):
    print("Bad command")
  if cmd[0] == 'cd':
    os.chdir(cmd[1])
    if cmd[1] == '.':
      os.chdir(home)
  if cmd[0] == 'ddir':
    shutil.rmtree(cmd[1])
  if cmd[0] == 'start':  
    os.system("exec" + cmd[1:])
  if cmd[0] == 'java':
    os.system(f"java {cmd[1]}")
  if cmd[0] == 'help':
    print("\nstart: starts a program)\necho: echos the following text\ndir: shows all files in a directory\ndel: deletes a file\nopen: shows contents of a file\nmakedir: creates the following directory inside the current directory\ncd: changes directory to the following dir\nddir: deletes the following dir\nrename: renames a file or directory\nclone: clones a file or directory to a certain dir\njava: runs a java program\nmove: moves a file to a requested directory\npython3: starts a python 3 program\ndate: shows current date\ntime: shows current time\nsetDate: sets date to the following. Format is 'year, month, day'\nexit: exits Py-DOS")
  if cmd[0] == 'rename':
    os.rename(cmd[1], cmd[2])
  if cmd[0] == 'clone':
    shutil.copy2(cmd[1], cmd[2])
  if cmd[0] == 'move':
    shutil.move(cmd[1], cmd[2])
  if cmd[0] == 'date':
    date = today.strftime("%m/%d/%y")
    fullDate = today.strftime("%B %d, %Y")
    print(date + "\n" + fullDate)
  if cmd[0] == 'time':
    time = now.strftime("%H"+":%M" + "(Time is in GMT +0)")
    print(time)
  if cmd[0] == 'setDate':
    today = datetime(int(cmd[1]), int(cmd[2]), int(cmd[3]))
  if cmd[0] == 'exit':
    os.system(exit)
