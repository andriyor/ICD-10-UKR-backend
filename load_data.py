import json

import sqlalchemy

from icd_10_app import models
from icd_10_app.database import SessionLocal, engine

sqlalchemy.orm.configure_mappers()
models.Base.metadata.create_all(bind=engine)
db = SessionLocal()


def traverse_tree(tree, prev_code=None):
    for code in tree:
        db_code = models.Code(code=code.get('code'), descriptionUA=code.get('descUA'), descriptionENG=code.get('descENG'))
        if prev_code:
            prev_code.child.append(db_code)

        codes = code.get('child')
        if len(codes):
            db_code.hasChild = True
            db.add(db_code)
            traverse_tree(codes, db_code)

    db.commit()


with open('resultTree.json') as json_file:
    data = json.load(json_file)
    traverse_tree(data)
