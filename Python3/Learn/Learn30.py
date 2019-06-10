# 错误处理机制 try...except...else...finally...
# 所有的错误类型都继承BaseException
import logging
try:
    print("try...")
    r = 10/int("2")
    print("result:", r)
except ValueError as e:
    print("ValueError", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
else:
    print("NO error")  # 没有错误时执行
finally:
    print("finally....")  # 最后执行

# try..except 多层捕捉错误


def foo(s):
    return 10/int(s)


def bar(s):
    return foo(s)*2


def main():
    try:
        bar("0")
    except Exception as e:
        print("Error:", e)
        logging.exception(e)  # 把错误记录到日志文件
    finally:
        print("finally...")


main()
