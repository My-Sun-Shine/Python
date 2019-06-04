# ORM框架的小实例
# ORM 对象-关系应收，把关系数据库的一行映射为一个对象，也就是一个类对于一行表


class Field(object):
    # 定义Field类
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        # 父类的__init__方法
        super(StringField, self).__init__(name, "vachar(100)")


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        print("found model:", name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("found mapping:%s => %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings  # 保存属性和列的映射关系
        attrs["__table__"] = name  # 表名和类名相同
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        field = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            field.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = "insert into %s(%s) values (%s)" % (
            self.__table__, ",".join(field), ",".join(params))
        print("SQL:", sql)
        print(str(args))


class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField("id")
    name = StringField("name")
    email = StringField("email")
    password = StringField("password")


u = User(id=1234, name="ABCD", email="test@qq.com", password="*****")
u.save()
