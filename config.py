DB_USERNAME = "root"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_NAME = "resume_scanner_db"
DB_PORT = "3306"

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
