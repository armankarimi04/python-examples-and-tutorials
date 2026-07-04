import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base

db = sa.create_engine("sqlite:///:memory:", echo=False)
Session = sessionmaker(bind=db) # sessionmaker() binds the engine to the session
Base = declarative_base() # manages the schema (because it contains the metadata)

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True) # mapped_column() to supply extra information
    username: Mapped[str]
    email: Mapped[str]
    
    def __repr__(self) -> str:
        return f'<User(id={self.id}, username={self.username}, email={self.email})>'
    
def main() -> None:
    Base.metadata.create_all(db)
    user = User(username="dude", email="dude@place.com")
    
    with Session() as session:
        session.add(user)
        session.commit()
        print(session.query(User).all())
        
if __name__ == "__main__":
    main()
