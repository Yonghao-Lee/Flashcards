#  write your code here 
file = open('/Users/yonghaolee/Python/Flashcards (Python)/Topics/Reading files/Summer/data/dataset/input.txt', 'r')
count = 0
for line in file:
    if line.strip() == 'summer':
        count += 1
file.close()
print(count)

