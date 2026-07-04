import sqlalchemy as sa

# create and open a sqlite database in RAM
engine = sa.create_engine("sqlite:///:memory:", echo=False) # by setting echo=True, more details will be outputted
connection = engine.connect()

metadata = sa.MetaData() # allows us to define an schema (structure of database)

user_table = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String),
    sa.Column("email", sa.String)
)

def insert_user(username: str, email: str) -> None:
    query = user_table.insert().values(username=username, email=email)
    connection.execute(query)
    
def select_user(username: str) -> sa.engine.Result:
    query = user_table.select().where(user_table.c.username == username)
    result = connection.execute(query)
    return result.fetchone()

def main() -> None:
    metadata.create_all(engine)
    insert_user("dude", "dude@place.com")
    print(select_user("dude"))
    connection.close()
    
if __name__ == "__main__":
    main()