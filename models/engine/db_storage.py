#!/usr/bin/python3
""" Context manager to connect the objects
to the database
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.base_model import BaseModel


env_vars = {
    'HBNB_ENV': None,
    'HBNB_MYSQL_USER': None,
    'HBNB_MYSQL_PWD': None,
    'HBNB_MYSQL_HOST': None,
    'HBNB_MYSQL_DB': None,
    'HBNB_TYPE_STORAGE': None
}


class_list = ['User', 'Place',
              'State', 'City', 'Amenity', 'Review']


class DBStorage():
    """Manage the connection bewteen database and the
    objects.
    """
    __engine = None
    __session = None

    def __init__(self):
        # asignar las variables de entorno al diccionario
        for k in env_vars.keys():
            env_vars[k] = getenv(k)

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(env_vars['HBNB_MYSQL_USER'],
                                                 env_vars['HBNB_MYSQL_PWD'],
                                                 env_vars['HBNB_MYSQL_HOST'],
                                                 env_vars['HBNB_MYSQL_DB']), pool_pre_ping=True)

   # Eliminar las tablas? -> defininedo un ambiente diferente o no cre
        if (env_vars['HBNB_ENV'] == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """add the object to the current database session
        Args:
            cls (class):for query on the current database session
            all objects depending of it  name

        Returns:
           dict_to_return [Dict]: Objects dictionary
        """

        # imports
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        # dict of class
        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        instances = list()
        if cls:
            instances = self.__session.query(classes[cls]).all()
        else:
            for k in classes.keys():
                try:
                    if (self.__session.query(classes[k]).all()) != []:
                        instances.extend(
                            self.__session.query(classes[k]).all())
                except:
                    pass

        dict_to_return = {}

        for object_ in instances:
            # es posible que sea v['__class__']
            name = object_.__class__.__name__
            id = object_.to_dict()['id']
            key = name + '.' + id
            dict_to_return[key] = object_

        return dict_to_return

    def new(self, obj):
        """add the object to the current database session

        Args:
            obj ([Object]): Object to add
        """

        self.__session.add(obj)
        self.save()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session

        Args:
            obj ([Object]): Object to remove

        Returns:
            [None]: If object not exist
        """
        # The database delete operation occurs upon flush().
        if obj:
            self.__session.delete(obj)
        else:
            return None

    def reload(self):
        """create all tables in the database and build the sessions"""
        # Revisar si hay que importar
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        # Possible bug -> check the scopped session
        Session = scoped_session(self.__session)
 #       Session = scoped_session(session)
        self.__session = Session()
