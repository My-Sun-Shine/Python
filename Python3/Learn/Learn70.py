from wsgiref.simple_server import make_server


def App(environ, start_response):
    # http://localhost:9500
    start_response("200 ok", [("Content-Type", "text/html")])
    return [b'<h1>Hello,Web</h1>']


def App1(environ, start_response):
    # http://localhost:9500/aaaa
    start_response("200 ok", [("Content-Type", "text/html")])
    # 抽取路径信息
    body = "<h1>Hello,%s</h1>" % (environ["PATH_INFO"][1:] or "Web")
    return [body.encode("utf-8")]


# environ是包括HTTP的请求信息，可以获取
httpd = make_server('', 9500, App1)
print("开始监听")
httpd.serve_forever()
