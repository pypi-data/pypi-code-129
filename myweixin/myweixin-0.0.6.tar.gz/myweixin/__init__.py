import time
import information
import requests


# url = "http://127.0.0.1:7777/DaenWxHook/httpapi/?wxid=wxid_at1vbqt6zgg922"
# data = {"type": "Q0003",
#         "data": {},
#         }
# r = requests.post(url=url, json=data)
# print(r.json())


class Robot:
    """
    weixin python

    """

    def __init__(self, url, wxid):
        self.url = url
        self.wxid = wxid

    def command(self, name):
        url = self.url
        data = {"type": "Q0003",
                "data": {},
                }
        r = requests.post(url=url, json=data)
        print(r.json())

    def post_(self, type_, data_):
        url = self.url
        r = requests.post(url=url, json=data_, params={"wxid": f"{self.wxid}"})
        # print(r.json())
        return r.json()

    def say(self, msg):
        type_ = "Q0001"
        data_ = {"type": f"{type_}",
                 "data": {"type": "1"},
                 }

        self.post_(type_, data_)

    def get_friend_list(self):
        type_ = "Q0005"
        data_ = {"type": f"{type_}",
                 "data": {"type": "1"},
                 }

        return self.post_(type_, data_)

    def get_group_chat(self):
        type_ = "Q0006"
        data_ = {"type": f"{type_}",
                 "data": {"type": "1"},
                 }

        return self.post_(type_, data_)

    def send_music_sharing(self, wxid, name, author, app, jumpUrl, musicUrl, imageUrl):
        type_ = "Q0014"
        data_ = {"type": f"{type_}",
                 "data": {"wxid": f"{wxid}",
                          "name": "我也",
                          "author": "无名",
                          "app": "wx8dd6ecd81906fd84",
                          "jumpUrl": "https://music.163.com/#/outchain/2/1851471702/",
                          "musicUrl": "https://m801.music.126.net/20220712225441/c29fc05bacb2bdb718c63292c0996424/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/9332483450/8200/5a0f/e1d3/3055c658f1c90e30edcb3aec2888f854.mp3",
                          "imageUrl": "https://huyaimg.msstatic.com/avatar/1016/b9/b6824c9d5593f03f5b5c4f71189023_180_135.jpg?1564815405"},
                 }

        return self.post_(type_, data_)


# a = Robot(url="http://127.0.0.1:7777/DaenWxHook/httpapi/", wxid="wxid_at1vbqt6zgg922")
# bbb=a.get_friend_list()
# print(bbb)
# import information
# if __name__ == '__main__':
#     information.run()
#     print(1)
#     print(information.q.get())

