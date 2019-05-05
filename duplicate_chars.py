from collections import defaultdict

def get_repeated_chars(s):
    count = {}
    for c in s:
      if c in count:
        count[c] += 1
      else:
        count[c] = 1

    freq = {}
    for k in count:
      if count[k] > 1:
          freq[k] = count[k]
    return freq


def get_repeated_chars2(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1

    for c in sorted(d, key=d.get, reverse=True):
      if d[c] > 1:
          print("{0} {1}".format(c, d[c]))

str = "thequickbrownfoxjumpsoverthelazydog"
print(get_repeated_chars(str), end = "\n\n")
print(get_repeated_chars2(str))
