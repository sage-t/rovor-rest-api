import sqlite3
from rovor_config import RovorConfig

class DBController:

  def __init__(self):
    self.config = RovorConfig()

  def getConnection(self):
    return sqlite3.connect(self.config.db_loc)
