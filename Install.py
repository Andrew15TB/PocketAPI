import os,shutil

def install_command():
    path = "C:\\Users\\" + os.getlogin() + "\\PacketAPI"
    info_text = '''
    {
        "name":"PacketAPI",
        "version":1.0,
        "path":"'''+path+'''",
        "alive":true,
        "install_pack":{}
    }
    '''
    os.mkdir(path=path)
    os.mkdir(path=path + "\\Cache")
    os.mkdir(path=path + "\\Temp")
    with open(path+"\\"+"info.json","w") as info:
        info.write(info_text)
    print("End!")
    #PIP Command

if __name__ == '__main__':
    print("Install 'PacketAPI'")
    t = input("Start?(y or n)")
    if t == "y":
        install_command()
    elif t == "n":
        print("EXIT!")
        exit()
    else:
        print("Error:i1")
