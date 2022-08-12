import random
import re

import requests
from tqdm.auto import tqdm
from sentence_splitter import SentenceSplitter, split_text_into_sentences
from .diff import dff_text


def get_markdown_images(text):
    """
    从markdown中提取图片

    :param text:
    :return:
    """
    image_arr = re.findall(r'(?:!\[(.*?)\]\((.*?)\))', text)  # 提最述与rul
    # print("image_arr", image_arr)
    return image_arr


def auto_request(payload, api, timeout=600):
    """

    :param api:
    :param payload:
    :param timeout:
    :return:
    """
    response = requests.request(
        "POST", api, json=payload, headers=None, timeout=timeout)
    # print(response.text)
    return response.json()


class SentenceClassification(object):
    """
    # 文本分类 请求接口

    """

    def __init__(self, api, timeout=30, **kwargs):
        self.api_host = api  # 服务器
        self.timeout = timeout  # 超时

    def predict_text_pet(self, text_list=[]):
        """


        :param text_list:  # 需要预测的文章列表
        :param timeout: #设置请求超时
        :return:
        """
        payload = {"config": {
            "max_length": 512,  #
        }, "text": text_list}
        api = f"{self.api_host}/predict_text_pet"
        return auto_request(payload, api, self.timeout)


class AutoReWrite(object):
    """
    # AutoReWrite 自动重写模块





    """

    def __init__(self, api='http://192.168.1.18:3008', **kwargs):
        self.api_host = api
        pass

    def auto_request(seld, payload, api, timeout=600):
        """
        请求封装

        :param api:
        :param payload:
        :param timeout:
        :return:
        """
        response = requests.request(
            "POST", api, json=payload, headers=None, timeout=timeout)
        # print(response.text)
        return response.json()

    def predict_paraphrase(self, payload, timeout=600):
        """
        生成同义句

        示例：

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            },"text": ["Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
                   "than a century ago in Britain. "]}
            out = predict_paraphrase(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict_paraphrase"
        return self.auto_request(payload, api, timeout)

    def predict_summary(self, payload, timeout=600):
        """
        生成摘要
        示例：

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            },"text": ["Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
                   "than a century ago in Britain. "]}
            out = predict_summary(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict_en_summary"
        return self.auto_request(payload, api, timeout)

    def auto_summary(self, text):
        """
        自动生成摘要，设置了默认参数

        获取最好的一个摘要信息



        示例：
            from tkitAutoRewriter import AutoReWrite, SentenceClassification
            text = "The Border Collie is a British breed of herding dog of medium size. They are descended from landrace sheepdogs once found all over the British Isles, but became standardized in the Anglo-Scottish border region. Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1] The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent domestic dog breeds.[2] Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets."
            # rewriter = AutoReWrite(api='http://192.168.1.18:3008')
            rewriter = AutoReWrite(api='http://127.0.0.1:3000')
            out = rewriter.auto_summary(text)
            print(out)
            > {'results': [[{'summary_text': 'Border Collie: Dog Breed Profile, Characteristics, and Development-Worthy of Homeward-Homeward Herding Dogs of the 21st-century Dog-Ages'}]]}

        :param text:
        :return:
        """
        payload = {"config": {
            "do_sample": False,
            # "num_beams": 5,
            "max_length": 256
            # "num_return_sequences": 5
        }, "text": [text]}
        return self.predict_summary(payload, timeout=600)
        # pass

    def predict_title(self, payload, timeout=600):
        """
        生成标题

        示例：

            payload = {"config": {
            "num_beams": 5,
            "max_length": 64,
            "num_return_sequences": 5
            },"text": ["Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
                   "than a century ago in Britain. "]}
            out = predict_paraphrase(payload)
            print(out)


        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict_headline_rewriter"
        return self.auto_request(payload, api, timeout)

    def auto_title(self, text):
        """
        自动生成标题，设置了默认参数

        示例：
            from tkitAutoRewriter import AutoReWrite, SentenceClassification
            text = "The Border Collie is a British breed of herding dog of medium size. They are descended from landrace sheepdogs once found all over the British Isles, but became standardized in the Anglo-Scottish border region. Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1] The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent domestic dog breeds.[2] Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets."
            # rewriter = AutoReWrite(api='http://192.168.1.18:3008')
            rewriter = AutoReWrite(api='http://127.0.0.1:3000')
            out = rewriter.auto_title(text)
            print(out)
            > {'results': [[{'summary_text': 'Border Collie: Dog Breed Profile, Characteristics, and Development-Worthy of Homeward-Homeward Herding Dogs of the 21st-century Dog-Ages'}]]}

        :param text:
        :return:
        """
        payload = {"config": {
            # "do_sample": False,
            "num_beams": 8,
            "max_length": 64,
            "num_return_sequences": 8
        }, "text": [text]}
        return self.predict_title(payload, timeout=600)
        pass

    def predict_paraphrase_sbert(self, payload, timeout=600):
        """
        预测句子相关性

        :param payload:
        :param api:
        :param timeout:
        :return:
        """
        api = f"{self.api_host}/predict_paraphrase_sbert"
        return self.auto_request(payload, api, timeout)

    def auto_paraphrase(self, payload={}):
        """
        自动生成同义句并自动筛选

            payload = {"config": {
            "num_beams": 5,
            "max_length": 120,
            "num_return_sequences": 5
            }, "text": [
            "Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
            "than a century ago in Britain. "]}
            auto_paraphrase(payload)

            结果如下

            > {'text': 'Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more than a century ago in Britain. ', 'text_pair': ['The Border Collie was developed more than a century ago in Britain.', 'The Border Collie was developed in Britain more than a century ago.', 'The Border Collie was developed over a century ago in Britain.', 'The Border Collie was developed in Britain over a century ago.', 'The Border Collie was developed more than a century ago in Britain and is a prize for his intelligence, herding instinct and working ability.'], 'out': {'results': {'scores': [0.8412754581989551, 0.8384939168488782, 0.8282370060160626, 0.8268469374505539, 0.9535872264040571], 'best_pair': 'The Border Collie was developed more than a century ago in Britain and is a prize for his intelligence, herding instinct and working ability.', 'best_pair_index': 4}}}


        :param payload:
        :return:
        """

        paraphrase = self.predict_paraphrase(payload)
        # print("同义句生成结果：",out)

        # can remove pre words
        # pre_arr = ["del summary paraphrase：", "summary paraphrase:",  "del：", "summary：", "paraphrase：",
        #            "summary paraphrase：", "del paraphrase：", "del summary paraphrase：", "del summary：", "paraphrase : ", "del summary："]
        pre_arr = ["del summary paraphrase：", "summary paraphrase:", "summary：", "paraphrase：", "summary paraphrase：",
                   "del paraphrase：", "del summary paraphrase：", "del summary：", "paraphrase : ", "del summary："]
        # 开始预测相关性最大的句子
        or_text = payload["text"][0]
        text_pair = []
        for it in paraphrase['results'][0][0]:
            # print(it.get("summary_text"))
            tx = it.get("summary_text").replace("\n", '')
            # 清理头
            for pre_text in pre_arr:
                if tx.startswith(pre_text):
                    tx = tx.replace(pre_text, '')
                tx = tx.replace(pre_text, '')
            # print(tx)
            text_pair.append(tx)

        if type(or_text) == str:
            for pre_text in pre_arr:
                # print(pre_text)
                if or_text.startswith(pre_text):
                    or_text = or_text.replace(pre_text, "")
        # print(or_text)
        payload = {"text": or_text, "text_pair": text_pair}

        out = self.predict_paraphrase_sbert(payload)
        # print("相关性最大的句子：",out)
        #
        # print("最终结果：")
        # print(or_text)
        # print(out['results']['best_pair'])
        payload['out'] = out
        return payload

    def rewriter(self, text, simlimit=0.8, num_beams=5, num_return_sequences=5, max_length=64, simlimitmax=1.0,
                 auto_sample=False, pre_text="del summary paraphrase：", **kwargs):
        """
        对文本进行重写,
        自动将文章拆分成句子，之后逐句生成同义句，
        使用逐句重写方案，后对句子的相关性进行判别

        :param pre_text:  # 重写模式 ["del summary paraphrase：", "del：", "summary：", "paraphrase：", "del summary paraphrase："]
        :param auto_sample: #是否随机选择，否则选择相关度最高的句子
        :param simlimitmax:  # 限制最大相关度
        :param max_length:  # 句子最大长度
        :param num_return_sequences:  #候选句子个数
        :param num_beams: #
        :param simlimit: # 相关度限制
        :param text:  # 输入的文本内容，不限制字数
        :return new:  返回生成句子列表
        """
        splitter = SentenceSplitter(language='en')
        # print(splitter.split(text='This is a paragraph. It contains several sentences. "But why," you ask?'))
        # ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']
        # ["del summary paraphrase：", "del：", "summary：", "paraphrase：", "del summary paraphrase："]

        newdata = []
        images_list = []
        for p in text.split('\n'):
            # 判断是否存在图片，如果存在图片则不做重写
            images = get_markdown_images(p)
            if len(images) == 0:
                for sent in tqdm(splitter.split(text=p)):
                    images = get_markdown_images(sent)
                    if len(sent) > 5 and len(images) == 0:
                        payload = {"config": {
                            "num_beams": num_beams,
                            "max_length": max_length,
                            "num_return_sequences": num_return_sequences
                        }, "text": [pre_text + sent]}
                        try:
                            # 预测同义句
                            out = self.auto_paraphrase(payload)
                            # print(out)
                            # print("\n\n")

                            best_pair_index = out['out']['results']['best_pair_index']
                            #  这里限制 相关度
                            if auto_sample == False and (
                                    simlimitmax > out['out']['results']['scores'][best_pair_index] > simlimit):
                                # print(out['text'], "\n==>\n", out['out']['results']['best_pair'])
                                newdata.append(
                                    out['out']['results']['best_pair'])
                            elif auto_sample == True:
                                # 筛选出匹配的index
                                pair_index = []
                                for i, score in enumerate(out['out']['results']['scores']):
                                    if simlimitmax > score > simlimit:
                                        pair_index.append(i)
                                    pass
                                index = random.choice(pair_index)
                                # print('pair_index:', index)
                                newdata.append(
                                    out["text_pair"][index].replace('\n', ''))
                                pass

                            else:
                                # print(out['text'], "\n==>\n", "相关度过低不休改")
                                newdata.append(sent)
                        except Exception as e:
                            newdata.append(sent)
                    else:
                        newdata.append(sent)
            else:
                newdata.append(p)
                images_list = images_list + images
            newdata.append("\n")
        # print(text, "\n")
        # print("".join(new), "\n")
        return {"items": newdata, "images": images_list}


if __name__ == "__main__":
    # payload = {"config": {
    #     "num_beams": 5,
    #     "max_length": 120,
    #     "num_return_sequences": 5
    # }, "text": [
    #     "Prized for his intelligence, herding instinct and working ability, the Border Collie was developed more "
    #     "than a century ago in Britain. "]}
    # out=auto_paraphrase(payload)
    # print(out)

    auto = AutoReWrite()
    splitter = SentenceSplitter(language='en')
    # print(splitter.split(text='This is a paragraph. It contains several sentences. "But why," you ask?'))
    # ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']
    text = """
    
    The Border Collie is a British breed of herding dog of medium size. They are descended from landrace sheepdogs once found all over the British Isles, but became standardized in the Anglo-Scottish border region. Presently they are used primarily as working dogs to herd livestock, specifically sheep.[1]

    The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent domestic dog breeds.[2] Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets.
    
    
    """

    new = []
    for sent in splitter.split(text=text):
        if len(sent) > 2:
            payload = {"config": {
                "num_beams": 5,
                "max_length": 120,
                "num_return_sequences": 5
            }, "text": [sent]}
            out = auto.auto_paraphrase(payload)
            # print(out)
            # print("\n\n")

            best_pair_index = out['out']['results']['best_pair_index']
            #  这里限制 相关度
            if out['out']['results']['scores'][best_pair_index] > 0.92:
                # print(out['text'], "\n==>\n", out['out']['results']['best_pair'])
                new.append(out['out']['results']['best_pair'])
            else:
                # print(out['text'], "\n==>\n", "相关度过低不休改")
                new.append(out['text'])
        else:
            new.append(out['text'])

    print(text, "\n")
    print("".join(new), "\n")

    dff = dff_text(text, "".join(new))
    print(dff, "\n")
