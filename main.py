from colorama import Fore, Back, Style
import os
import shutil
BOLD = '\033[1m'
print(Fore.BLUE + "Py-DOS 1.5\nCopyright 2020 Cooper\n")
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
  if not cmd[0] in ('start', 'echo', 'dir', 'del', 'open', 'makedir', 'cd', 'ddir', 'help', 'clone', 'rename', 'jvrun', 'move', 'cls'):
    print("Bad command")
  if cmd[0] == 'cd':
    os.chdir(cmd[1])
    if cmd[1] == '.':
      os.chdir(home)
  if cmd[0] == 'ddir':
    shutil.rmtree(cmd[1])
  if cmd[0] == 'start':  
    exec(open(cmd[1] + ".py").read())
  if cmd[0] == 'jvrun':
    os.system(f"java {cmd[1]}")
  if cmd[0] == 'help':
    print("\nstart: starts a program (python)\necho: echos the following text\ndir: shows all files in a directory\ndel: deletes a file\nopen: shows contents of a file\nmakedir: creates the following directory inside the current directory\ncd: changes directory to the following dir\nddir: deletes the following dir\nrename: renames a file or directory\nclone: clones a file or directory to a certain dir\njvrun: runs a java program\nmove: moves a file to a requested directory\ncls: clears all text on the screen\n")
  if cmd[0] == 'rename':
    os.rename(cmd[1], cmd[2])
  if cmd[0] == 'clone':
    shutil.copy2(cmd[1], cmd[2])
  if cmd[0] == 'move':
    shutil.move(cmd[1], cmd[2])
  if cmd[0] == 'cls':
    print ("\033[2J\033[H")