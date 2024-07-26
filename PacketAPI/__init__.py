import os,json,time

install_path = "C:\\Users\\"+os.getlogin()+"\\PacketAPI\\"
def make_path(packet_name):
    a = install_path + "cache\\" + packet_name
    b = install_path + "temp\\" + packet_name
    return [a,b]


# noinspection PyBroadException
# 下面可能会有点混乱
def Register(name:str,version:float,msg:str) -> int:
    try:
        c = make_path(name)

        with open(install_path+"info.json","r",encoding="utf-8") as book:
            text = json.load(book)
            print(text)
            text["install_pack"][name] = '{"version":'+str(version)+',"msg":'+msg+',"cache":'+c[0]+',"temp":'+c[1]+'}'
            print(text)
            book.close()
        with open(install_path+"info.json","w",encoding="utf-8") as book2:
            json.dump(text,book2,ensure_ascii=False)
            book2.close()
    except:
        return 1
    else:
         return 0
    
def Uninstall(name):
    pass

class Cache(object):
    def __init__(self,packet_name:str) -> None:
        self.ctrl_dir = make_path(packet_name)[0]
        self.ctrl_pack = packet_name
        os.mkdir(self.ctrl_dir)
    def new(self):
        d = str(time.time())[0:9]
        os.mkdir(d)
        self.work_dir = d
    def write(self,file_n:str,file_t):
        with open(self.ctrl_dir+self.work_dir+file_n,"w") as f:
            f.write(file_t)
            self.f = f
    def get(self):
        return self.f
    def clear(self):
        for i in os.listdir(self.ctrl_dir):
            os.removedirs(i)
