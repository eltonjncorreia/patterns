from .singleton import SingletonMeta


class DataBase(metaclass=SingletonMeta):
    connection: str = ""

    def __init__(self, connection_string: str) -> None:
        self.connection = connection_string


def test_create_connection():
    db1 = DataBase(connection_string="string-connection")
    db2 = DataBase(connection_string="other-connection")

    assert db1.connection == "string-connection"
    assert db2.connection == "string-connection"
    assert id(db2) == id(db2)
