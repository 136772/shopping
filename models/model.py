from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random
import os
import time

Base = declarative_base()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class User(Base):
    __tablename__ = 'user'

    tmTel = Column(String(20), primary_key=True)
    tmPwd = Column(String(20))
    date = Column(String(20))
    money = Column(String(20))


class DbControl(object):
    def __init__(self):
        print('sqlite:///'+BASE_DIR+'/weikegu.db')
        self.engine = create_engine('sqlite:///'+BASE_DIR+'/weikegu.db', echo=True)
        self.DBSession = sessionmaker(bind=self.engine)

    def __fromattime__(self):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    def creatuser(self, tmTel, money, date, tmPwd='242628'):
        try:
            session = self.DBSession()
            newuser = User(tmTel=tmTel, tmPwd=tmPwd, date=date, money=money)
            session.add(newuser)
            session.commit()
            session.close()
            return '成功'
        except Exception as e:
            print(e)
            return '保存失败'

    def searchuser(self):
        userlist = []
        try:
            session = self.DBSession()
            date = self.__fromattime__()
            user = session.query(User).filter(User.date < date).all()
            session.close()
            if len(user) > 15:
                temp = 15
            else:
                temp = len(user)

            while len(userlist) != temp:
                u = random.choice(user)
                if u.tmTel not in userlist:
                    userlist.append(u.tmTel)
            return userlist
        except Exception as e:
            print(e)
            return

    def edituser(self, tmTel):
        try:
            session = self.DBSession()
            date = self.__fromattime__()
            session.query(User).filter(User.tmTel == tmTel).update({'date': date})
            session.commit()
            session.close()
            return '数据保存成功'
        except Exception as e:
            print(e)

    def datareport(self):
        try:
            session = self.DBSession()
            date = self.__fromattime__()
            user = session.query(User).filter(User.date == date).all()
            session.close()

            return user
        except Exception as e:
            print(e)
            return

if __name__ == '__main__':
    db = DbControl()
    # print(db.edituser('13301157611'))
    # users = db.searchuser()
    # print(users)
    # for i in users:
    #     print(i.tmTel)
    #
    #
    # import os
    #
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # with open(BASE_DIR + '/userlist', 'r') as f:
    #     while 1:
    #
    #         line = f.readline()
    #         if not line:
    #             break
    #         print(db.creatuser(line, '9000', '2016-11-05'))
