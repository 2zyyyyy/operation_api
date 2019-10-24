# @File:getAesCode.py
# @Author:2zyyyyy
# @Time:2019年05月23日
# @Explain: 实现加密方法
import datetime
import hashlib
import random
import string

from Crypto.Cipher import AES
import time


class AesCode:
    # 秘钥
    AesCode = "ccw.dev.123QWE!@#"
    KEY_ALGORITHM = "AES"
    CIPHER_ALGORITHM = "AES"

    # @staticmethod
    def get_aes_code(self):
        # 创建一个随机字符串 长度为指定的字符数() 字符将从拉丁字母（a-z、A-Z）和数字0-9中选择
        echostr = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(4)])
        # 为变量赋随机值1000-9999
        nonce = ''.join(str(i) for i in random.sample(range(0, 9), 4))
        # 获取当前时间 格式为'yyyy-MM-dd HH:mm:ss'
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 验证签名证书 signature 验证时间戳 timestamp 当前随机数 nonce 当前随机字符串 echostr 组合形式为：
        # （echostr 初始字段MD5加密） +（timestamp初始字段MD5加密）+（ MD5加密nonce）
        singature = self.md5(echostr) + self.md5(timestamp) + self.md5(nonce)
        aescode = 'singature=' + singature + '&echostr=' + "2个加密后参数" + '%nonce=' + nonce
        return echostr, nonce, timestamp, aescode

    def aes_encrypt_cbc(text, key, iv, block_size=16):
        '''
        这里密钥长度必须为16（AES-128）,24（AES-192）,或者32 （AES-256）Bytes 长度
        需要将传入的text,key,iv都转为bytes类型，否则在python3.6中会报错：TypeError:
        Object type <class 'str'> cannot be passed to C code
        :param text: 需加密的文本
        :param key: 密钥
        :param iv: 模式为CBC时，需指定偏移量
        :param block_size: 可以是8,16,32,64
        :return: 16进制字符串
        '''
        from Crypto.Cipher import AES
        key = key.encode()
        btext = text.pkcs7_pad(text, block_size).encode()
        iv = iv.encode()
        cryptor = AES.new(key, AES.MODE_CBC, iv)
        encrypt_text = cryptor.encrypt(btext)
        return encrypt_text

    def pkcs7_pad(text, length):
        count = len(text)
        pad_size = length - (count % length)
        text = text + (chr(pad_size) * pad_size)
        return text

    # 获取字符串的md5加密
    def md5(str):
        if type(str) is not bytes:
            str = str.encode('utf-8')
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()


if __name__ == '__main__':
    aes = AesCode().get_aes_code()
    print(aes[3])
