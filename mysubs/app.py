""" Module with final APP class"""
from .files import Files


class App(Files):
    """ App class """
    def __str__(self):
        """ Return student's name & id as repr?"""
        pass


if __name__ == "__main__":
  app = App()  # For testing to separate auth errors from app errors