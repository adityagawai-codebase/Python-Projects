text = "Python is very useful. I is easy to learn. Python is powerfull!"


def clean_text(text):
  word = text.replace(". !","")
  word = word.lower()
  word = word.split()

  return word


def count_frequecy(word):
  dic_word = {}
  for i in word:
      dic_word[i] = 0
  for i in word:
    if i in dic_word:
      dic_word[i] = dic_word[i] + 1
    else:
      dic_word[i] = 1

  return dic_word

def longest_word(words):
  max_word = ""
  for word in words:
    if len(word) > len(max_word):
      max_word = word

  return max_word

def shortest_word(words):
  min_word = words[0]
  for word in words:
    if len(min_word) > len(word):
      min_word = word

  return min_word


def average_length(word):
  total_length = 0
  for i in word:
    total_length += len(i)
  avg = int(total_length/len(word))

  return avg


word = clean_text(text)
# print(word)
# print(count_frequecy(word))
# print(longest_word(word))
# print(shortest_word(word))
# print(average_length(word))

def menu():
  print("Test Analysis Report \n ------------------")
  print(f"Total Words          :{len(word)}")
  print(f"Unique words         :{len(set(word))}")
  print(f"Logest word          :{longest_word(word)}")
  print(f"Shortest word        :{shortest_word(word)}")
  print(f"Average Length       :{average_length(word)}")

menu()


