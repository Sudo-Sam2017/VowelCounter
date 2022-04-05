file = open("VowelTarget.txt")

line = file.read().replace("\n", " ")
file.close()

print(line)
count = len(line)
print('Number of Characters in this text file: ' + str(count))

vowelList = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']

vowelCount = 0
consanantCount = 0

for element in line:
    if(element in vowelList):
        vowelCount = vowelCount + 1
    else:
        consanantCount = consanantCount + 1

print("Vowels: " + str(vowelCount))
print("Consanants: " + str(consanantCount))