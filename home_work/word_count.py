import numpy

# words_np=numpy.array(words)

words = ['a', 'b', 'a', 'a', 'c', 'd', 'd', 'd', 'd']

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

result = sorted(word_count.items(), key=lambda k: k[1], reverse=True)
print(result)

