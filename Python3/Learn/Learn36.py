# 序列化
import json
import pickle

d = dict(name="bob", age=15, score=100)

dict_b = pickle.dumps(d)
print(dict_b)
print(pickle.loads(dict_b))  # 反序列化
print("-"*30)
# Python类型所对应的的JSON类型：dict=>{},list=>[],str=>"string",int或float=>1234.2,True/False=>true/false,None=>null
dict_j = json.dumps(d)
print(dict_j)
print(json.loads(dict_j))  # 反序列化
print("-"*30)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return{
        "name": std.name,
        "age": std.age,
        "score": std.score
    }


def dict2student(d):
    return Student(d["name"], d["age"], d["score"])


s = Student("bob", 20, 100)
# 可选参数default 就是任意对象转换为可序列为json的对象
# dumps本身有很多可选参数
class_j = json.dumps(s, default=student2dict)
print(class_j)
print("-"*30)
print(json.dumps(s, default=lambda obj: obj.__dict__))
print("-"*30)
print(json.loads(class_j, object_hook=dict2student))  # 反序列化
print("-"*30)

obj = dict(name="小米", age=20)
print(json.dumps(obj, ensure_ascii=True))  # 是否进行ASCII编码
print(json.dumps(obj, ensure_ascii=False))
