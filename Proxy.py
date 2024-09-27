from abc import abstractmethod

# 定义抽象基类
class Proxy():

    # 注册
    @abstractmethod
    def register(self):
        pass

    # 上传
    @abstractmethod
    def upload(self):
        pass

    # 下载
    @abstractmethod
    def download(self):
        pass

    # 访问
    @abstractmethod
    def getURL(self):
        pass