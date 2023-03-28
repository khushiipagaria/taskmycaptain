def most_frequent(string):

  d = dict()

  for key in string:

    if key not in d:

      d[key] = 1

    else:

      d[key] += 1

  return d

word=input("enter word to check")

print( most_frequent(word))