import os
# f=open("demo.txt", "r")

# data=f.read()

# print(data)
# print(type(data))
# f.close()




# f=open("demo.txt", "a")
# f.write=("I wanr to learn java")

# f.close()

# f=open("demo.txt", "w+")
# f.write("abc")
# print(f.read())
# f.close()


# with open("demo.txt", "r") as f:
#     data=f.read()
#     print(data)

# with open ("demo.txt", "w")as f:
#     f.write("new data")
    
#     os.remove("sample.txt")


# with open("practice.txt", "r")  as f:
#     # f.write("Hi everyone\nwe are learning File I/O\n")
#     # f.write("using Java.\nI like programming in Java.")
    
#     data=f.read()

# new_data=data.replace("java", "python")
# print(new_data)


def check_for_word():
    word ="pyq"
    data=True
    line_no=1
    with open ("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
            return
        line_no+=1
    return -1
    
print(check_for_word())