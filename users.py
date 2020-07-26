# испортируем модули стандартнй библиотеки uuid и datetime
import uuid
import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()


class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'user'
    id = sa.Column(sa.String(36), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    email = sa.Column(sa.Text)  
    gender = sa.Column(sa.Text)  
    height = sa.Column(sa.Float)  
    birthdate = sa.Column(sa.Text)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введи имя: ")
    last_name = input("Введи фамилию: ")
    email = input("Введи адрес электронной почты: ")
    gender = input("Введи свой пол: ")
    height = input("Введи свой рост в сантиметрах (пр. 179): ")
    birth_date = input("Введи дату рождения в формате YYYY-MM-DD: ")   
    # генерируем идентификатор пользователя и сохраняем его строковое представление
    user_id = str(uuid.uuid4())
    # создаем нового пользователя
    user = User(
        id=user_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender=gender,
        height=height,
        birthdate=birthdate
    )
    # возвращаем созданного пользователя
    return user


def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Спасибо, данные сохранены!")

if __name__ == "__main__":
    main()