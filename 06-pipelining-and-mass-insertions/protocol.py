"""
  protocol.py - Script generates Redis Protocal for mass insertation of
  10,000 key-values.

"""
__author__ = "Jeremy Nelson"
__license__ = "GPLv3"
import sys

def encode(value):
    if not type(value) == bytes:
        value = value.encode()
    return value

def gen_redis_proto(*cmd):
    proto = ""
    proto += "*" + str(len(cmd)) + "\r\n"
    for arg in map(encode, cmd):
        proto += "$" + str(len(arg)) + "\r\n"
        proto += arg + "\r\n"
    return proto

def main():
    for i in range(0, 10000):
        sys.stdout.write(gen_redis_proto(
            "SET",
            "Key:{}".format(i),
            "Value={}".format(i)))


if __name__ == '__main__':
    main()
