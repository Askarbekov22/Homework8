import sqlite3

data_basa = sqlite3.connect("Tables.db")
sql = data_basa.cursor()
data_basa.execute("""CREATE TABLE IF NOT EXISTS users(
    \'6-9\' TEXT,
    \'9-12\' TEXT,
    \'12-15\' TEXT,
    \'15-18\' TEXT,
    \'18-21\' TEXT,
    \'21-24\' TEXT,
    \'24-6\' TEXT
    )
    """
)
data_basa.commit()

