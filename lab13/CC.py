class Count:
  def __init__(self, name):
    self.fileName = name
    self.lines = 0
    self.words = 0
    self.chars = 0
  
  def counting(self):
    file = open(self.fileName)
    for line in file:
      words = line.split()
      self.lines += 1
      self.words += len(words)
      self.chars += len(line)
    
    file.close()
  
  def print(self):
    print('lines: ', self.lines, ' words: ', self.words,  ' chars: ',self.chars)

  @staticmethod
  def wc(*files):
    filesList = []
    for file in files:
      filesList.append(Count(file))
    
    sum_lines = 0
    sum_words = 0
    sum_chars = 0
    for it in filesList:
      print(it.fileName)
      it.counting()
      sum_lines += it.lines
      sum_words += it.words
      sum_chars += it.chars
      it.print()
    print('Razem: lines: ', sum_lines, ' words: ', sum_words,  ' chars: ',sum_chars)


test = Count("AA.py")
# test.counting()
# test.print()
test.wc("AA.py", "BB.py")