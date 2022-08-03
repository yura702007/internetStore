# компоненты библиотеки для описания структур таблицы
from sqlalchemy import Column, String, Integer, Boolean
# класс-конструктор для работы в декларативном стиле с SQLAchemy
from sqlalchemy.ext.declarative import declarative_base

# инициация декларативного стиля
Base = declarative_base()


class Category(Base):
    """
    Класс-модель для описания таблицы "Категория товара",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'category'
    # поля таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    is_active = Column(Boolean)

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса
        """
        return self.name
