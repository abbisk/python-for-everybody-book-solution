# Solution by Abhishek Kumar

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colpos = line.find(':')
        number = line[colpos+1:].strip()    # Removes all text except number
        SPAM_C = float(number)
        total = total + SPAM_C

average = total / count
print('Average spam confidence:', average)