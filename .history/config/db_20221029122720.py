from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/disqueria")

conn = engine.connect()

meta_data = MetaData()