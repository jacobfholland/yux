class Parent(Base):
    __tablename__ = 'parent'
    id = db.Column(Integer, primary_key=True)
    children = db.relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = 'child'
    id = db.Column(Integer, primary_key=True)
    parent_id = db.Column(Integer, ForeignKey('parent.id'))
    parent = db.relationship("Parent", back_populates="children")
