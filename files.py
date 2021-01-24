# Reading and output into a file
f = open('input.txt', 'r')
outFile = open('output.txt', 'w')
for index, line in enumerate(f):
    line_split = line.split()
    if line_split[2] == 'P':
        outFile.write(line)
f.close()
outFile.close()
