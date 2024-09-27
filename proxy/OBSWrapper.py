# coding: utf-8
import os
import logging
from Proxy import Proxy

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.http_handler import HttpHandler
from huaweicloudsdkvpc.v2 import VpcClient, ListVpcsRequest
from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion
from huaweicloudsdkcore.exceptions import exceptions

# 定义具体子类
class OBS(Proxy):

    # 构造函数
    def __init__(self, oss_ak, oss_sk, oss_endpoint):
        self.oss_ak = oss_ak
        self.oss_sk = oss_sk
        self.oss_endpoint = oss_endpoint
        self.register()

    def register(self):
        # 配置认证信息
        # 推荐通过环境变量等方式配置认证信息，参考2.4认证信息管理章节
        credentials = BasicCredentials(self.oss_ak, self.oss_sk)

        # 创建服务客户端
        client = VpcClient.new_builder() \
            .with_credentials(credentials) \
            .with_region(VpcRegion.value_of("cn-north-4")) \
            .build()

        # 发送请求并获取响应
        try:
            request = ListVpcsRequest()
            response = client.list_vpcs(request)
            print(response)
        except exceptions.ClientRequestException as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error_code)
            print(e.error_msg)
