from Proxy import Proxy

# 定义具体子类
class Cos(Proxy):

    #
    def __init__(self, filename):   # 构造函数，接收一个参数filename
        self.filename = filename    # 文件名保存在filename实例变量中
        self.load_from_disk()

    '''从磁盘中加载图片数据,子类RealImage独有的方法,由于这个过程比较耗时，因此需要在初始化时进行加载，避免在图片显示时等待'''
    def load_from_disk(self):  #
        print("loading " + self.filename)

