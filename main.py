import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="mydatabase"
)
mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE User (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE NOT NULL, email VARCHAR(255) UNIQUE NOT NULL)")

mycursor.execute("CREATE TABLE Profile (id INT PRIMARY KEY, user_id INT UNIQUE, bio TEXT, profile_picture VARCHAR(255), FOREIGN KEY (user_id) REFERENCES User(id))")







# ----------------------------------------------------

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('mysql+mysqlconnector://username:password@localhost/mydatabase')
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    profile = relationship("Profile", uselist=False, back_populates="user")

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), unique=True)
    bio = Column(Text)
    profile_picture = Column(String(255))
    user = relationship("User", back_populates="profile")

Base.metadata.create_all(engine)
