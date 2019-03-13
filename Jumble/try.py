import random
import string


def list_string(strn):
  level=[]
  def permute(prefix, suffix):
    level.append(prefix)
    if len(suffix)==0:
       return
    for i in range(len(suffix)):
      permute(prefix + suffix[i], suffix[:i]+suffix[i+1:])
  permute("",strn)
  return level

t = list_string("rtagryw")
print(type(t))


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

hmm=load_words()
print(type(hmm))

x=[]

for i in range(len(t)):
	if t[i] in hmm:
		x.append(t[i])

print(len(hmm))
print(len(x))
x=set(x)
print(sorted(x))
