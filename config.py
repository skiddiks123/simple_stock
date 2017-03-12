import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True  
SQLALCHEMY_DATABASE_URI = 'mysql://root:32167@portal/simple_stock'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
THREADS_PER_PAGE = 2
CSRF_ENABLED     = True
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"