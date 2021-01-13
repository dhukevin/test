#/usr/bin/python3
GPIO_NUM = 23
COLUMN_LEN = 16
COLUMN_GAP = 14


def read_file():
    file = open("line")
    count = 0
    while 1:
        for i in range(GPIO_NUM):
            count = count + 1
            if count >= GPIO_NUM * COLUMN_LEN:
                return
            line = file.readline()
            if not line:
                file.close()
                return
            line = line.strip()
            print(line)
            l[i].append('"' + line + '"')


def write_file():
    out = open("out" , "w")
    
    for subl in l:
        out.write("{")
        count = 0
        for str in subl:
            spaceCount = 0
            if len(str) < COLUMN_GAP:
                spaceCount = COLUMN_GAP - len(str)
            out.write(str + "," + spaceCount * " ")

            count = count + 1
            if count % 3 == 0:
                count = 0
                out.write("\n")

        out.write("},\n\n")

    out.close()
       
l = []
for i in range(GPIO_NUM):
    l.append([])

read_file()
write_file()


