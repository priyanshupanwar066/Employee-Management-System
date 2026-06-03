import os

class Config:
    """Application configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///employees.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 5000
