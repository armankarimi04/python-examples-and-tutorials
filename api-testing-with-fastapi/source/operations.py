from sqlalchemy.orm import Session
from main_with_dependecy import DBItem

# this file is similar to services.py
# purpose is to separate the endpoint and all the logic code for better teting

class NotFoundError(Exception):
    pass

# an example
def db_find_item(item_id: int, session: Session) -> DBItem:
    db_item = session.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise NotFoundError("Item Not found") # We're not returning an HTTP Exception, because that is part of the API, we're simply returning a custom 404 exception
    return db_item


# the rest is omitted