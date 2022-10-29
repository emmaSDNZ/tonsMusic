from sqlalchemy import create_engine, MetaData

engie = create_engine("mysql+pymysql://root:1234@localhost:3306/disqueria")