# @File:test.py
# @Author:2zyyyyy
# @Time:2019年05月24日
# @Explain:
import hashlib
import random
import string
import time


def get_encrypt_aes_str():
    aes_key = "ccw.dev.123QWE!@#"
    aes_key_md5 = get_str_md5(aes_key)
    print(aes_key_md5)

    echostr = random.sample(string.ascii_letters + string.digits, 4);
    nonce = random.sample(string.digits, 4)
    # 获取当前时间 格式为'yyyy-MM-dd HH:mm:ss'
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    echostr = 'abcd'
    timestamp = '2019-05-24 16:59:50'
    nonce = '1234'

    signature = get_str_md5(echostr) + get_str_md5(timestamp) + get_str_md5(nonce)
    echostr_encrypt = aes_encrypt_ecb(echostr, aes_key_md5).hex()
    print('加密后的echostr:', echostr_encrypt)
    timestamp_encrypt = aes_encrypt_ecb(timestamp, aes_key_md5).hex()
    print('加密后的timestamp:', timestamp_encrypt)

    text = "signature=" + signature + "&echostr=" + echostr_encrypt + "&timestamp=" + \
           timestamp_encrypt + "&nonce=" + nonce
    return text


# 获取字符串的md5加密
def get_str_md5(str):
    if type(str) is not bytes:
        str = str.encode('utf-8')
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


def aes_encrypt_ecb(text, key, block_size=16):
    '''
    aes encrypt with ecb mode
    :param text: text to encrypt
    :param key: key size should be times of 8
    :param block_size: block size
    :return:
    '''
    from Crypto.Cipher import AES
    key = key.encode()
    text = pkcs7_pad(text, block_size).encode()
    cryptor = AES.new(key, AES.MODE_ECB)
    encrypt_text = cryptor.encrypt(text)
    return encrypt_text


def pkcs7_pad(text, length):
    count = len(text)
    pad_size = length - (count % length)
    text = text + (chr(pad_size) * pad_size)
    return text


if __name__ == '__main__':
    res = get_encrypt_aes_str()
    print(res)
