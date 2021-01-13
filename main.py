print('Spelling List Program')
filename = ''
def use():
  filename = input('What filename do you want: ')
  filename = filename + ".txt"
  print(filename)
  c = open(filename,"r")
  c.close()
  return filename

def create():
  filename = input('What filename do you want: ')
  filename = filename + ".txt"
  print(filename)
  c = open(filename,"w")
  c.close()
  return filename

def add():
  word = input('Enter a spelling word: ')
  f = open(filename,"r")
  complete = f.read()
  print('the old list')
  print(complete)
  ls = complete.split('\n')
  print(ls)
  f.close()
  if word in ls:
    print(word + ' is already in the list.')
  else:
    f = open(filename,"a")
    f.write(word + '\n')
    f.close()
  
def show():  
  g = open(filename,"r")
  s = g.read()
  print(s)
  g.close()

def delete():
  word = ''
  word = input('Enter a word to delete: ')
  f = open(filename,"r")
  complete = f.read()
  print('the old list')
  print(complete)
  ls = complete.split('\n')
  print(ls)
  ls.remove(word)
  print(ls)
  f.close()
  f = open(filename, 'w')
  for w in ls:
    if len(w) > 0:  
      f.write(w + '\n')
  f.close()

def alphabetize():
  f = open(filename, 'r')
  complete = f.read()
  ls = complete.split('\n')
  ls.sort()
  f.close()
  f = open(filename, 'w')
  for w in ls:
    if len(w) > 0:  
      f.write(w + '\n')
  f.close()

  
while(True):
  try:
    print('Press O to open a previous list: ')
    print('Press C to create a new list: ')
    print("Press A to add a word: ")
    print("Press S to show all words: ")
    print("Press D to delete a word: ")
    print('Press B to alphabetize the spelling list: ')
    print("Press E to exit: ")
    task = input()
    if task.upper() == 'O':
      filename = use()
    if task.upper() == 'C':
      filename = create()
    if task.upper() == 'A':
      add()
    if task.upper() == 'S':
      show()
    if task.upper() == 'D':
      delete()
    if task.upper() == 'B':
      alphabetize()
    if task.upper() == 'E':
      break
  except:
    print("That is not a choice, try again!")
print('Your list has been saved.')
