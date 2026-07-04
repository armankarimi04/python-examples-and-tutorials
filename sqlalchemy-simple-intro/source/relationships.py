import hashlib
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base, relationship

db = sa.create_engine("sqlite:///:memory:", echo=False)
Session = sessionmaker(bind=db) # sessionmaker() binds the engine to the session
Base = declarative_base() # manages the schema (because it contains the metadata)

# one to one relationship User -> UserAuth

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True) # mapped_column() to supply extra information
    
    auth: Mapped["UserAuth"] = relationship( # notice that auth is not a mapped_column but a relationship
        "UserAuth", 
        uselist=False, # this indicates that we're mapping to a single object, hence one to one relationship
        back_populates='user' # syncs the relationship with the other side (in this case user row of UserAuth)
    )
    
    posts: Mapped[list["UserPost"]] = relationship(
        "UserPost", 
        back_populates='user'
    )
    
    def __init__(self, username: str, email: str, password: str):
        super().__init__()
        self.auth = UserAuth(username=username, email=email)
        self.auth.set_password(password)
    
    def __repr__(self) -> str:
        return f'<User(id={self.id}, username={self.auth.username}, email={self.auth.email})>'
    
    
class UserAuth(Base):
    __tablename__ = "user_auth"
    id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("users.id"), primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(index=True, unique=True)
    password_hash: Mapped[str]
    user: Mapped["User"] = relationship("User", back_populates="auth")
    
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        
    def set_password(self, password: str) -> None:
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        
    def check_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()
    
    def __repr__(self) -> str:
        return f"<UserAuth(username={self.username}, email={self.email})>"
    

class UserPost(Base):
    __tablename__ = "user_posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True)
    content: Mapped[str]
    user: Mapped["User"] = relationship("User", back_populates="posts")
    
    def __repr__(self) -> str:
        return f"<UserPost(user={self.user}, content={self.content})>"
    
    
def main() -> None:
    Base.metadata.create_all(db)
    
    # Using sessions with context managers is helpful, because we don't forget to commit or rollback changes
    
    with Session.begin() as session:
        user = User(username='dude', email='dude@place.com', password='password')
        post = UserPost(content="Hello World", user=user)
        session.add(user)
        session.add(post)
        
    with Session.begin() as session:
        user = session.query(User).first()
        print(user)
        print(user.auth)
        print(user.posts)
        
        print(f"Password check: {user.auth.check_password('password')}") # true
        print(f"Password check: {user.auth.check_password('wrongpassword')}") # false
        
        posts = session.query(UserPost).filter(UserPost.user == user).all()
        print(posts)
    
        
if __name__ == "__main__":
    main()
