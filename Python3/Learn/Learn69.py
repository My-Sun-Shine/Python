# sqlalchemy模块，Python中的ORM框架
from sqlalchemy import Column, String, create_engine, INT, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


class User(Base):
    # 定义User对象
    'User'
    __tablename__ = "user"  # 表的名字

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    score = Column(INT)
    # 1对多
    #books = relationship("Book")


class Book(Base):
    __tablename__ = "book"
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # "多"的一方book表示通过外键关联到user表
    user_id = Column(String(20), ForeignKey("user.id"))


# 初始化数据库连接
engine = create_engine(
    "mysql+mysqlconnector://root:123456@localhost:3306/test")
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

session = DBSession()
user = session.query(User).filter(User.id == "A-001").one()
print(user, type(user))
print(user.name, user.id, user.score)
session.close()
