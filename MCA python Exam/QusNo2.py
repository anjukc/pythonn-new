file_obj = open('textfile.txt','r+')
condition = True
print("starting with capital letter and word count greater than 5 is:")
while condition:
    line = file_obj.readline()
    words = line.split(" ")
    if(len(words)>5):
        x = words[0]
        if(x[0].isupper()):
            print(line)
    if not line:
        condition = False
        print("end of the file")
