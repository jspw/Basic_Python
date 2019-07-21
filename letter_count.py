def letter_count(word):
    count = {}
    for i in word:
        count[i] = word.count(i)
    return count

new = (letter_count("mehedi hasan shifat").items())
for i,j in new:
    print("'{}' -> {} times".format(i,j))

print(len(new))
