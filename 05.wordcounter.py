text = "python is very usefull language. it is my fav language. my name is  aditya bhimrao gawai son of bhimrao babarao gawai son of babarao shivram jankiram gawai"
words_count = {}
def clean_and_split(text):
  text = text.replace(".","")
  word = text.split()
  for i in word:
    words_count[i] = 0

  return word
  

def coutning_word_freq(word):
  count = 0
  for i in word:
    if i in words_count:
      words_count[i] = words_count[i] + 1
    else:
      words_count[i] = 1

  return words_count
   

def sorting(word):
  sort = []
  for i in word.items():
    sort.append(i)

  new_sort = sorted(sort,key=lambda x:x[1],reverse=True)
  new_sor = []
  for i in range(3):
    new_sor += new_sort[i]
  print(new_sor)
  
    

word = clean_and_split(text)
sorting(coutning_word_freq(word))

