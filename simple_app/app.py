import streamlit as st
from orm import Category, Product, create_engine
from sqlalchemy.orm import sessionmaker

# boilerplate code
def opendb():
    engine = create_engine('sqlite:///db.sqlite', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def closedb(session):
    session.commit() # save changes
    session.close()

# category add function
def add_category(name):
    db = opendb()
    obj = Category(name=name)
    db.add(obj)
    closedb(db)

def view_categories():
    db = opendb()
    categories = db.query(Category).all()
    return categories

def add_product(name, category):
    db = opendb()
    obj = Product(name=name, category=category)
    db.add(obj)
    closedb(db)

def view_products():
    db = opendb()
    products = db.query(Product).all()
    return products

st.title("SQLAlchemy Demo")

# add category
form = st.form(key='add_category')
name = form.text_input(label='Category Name')
submit = form.form_submit_button(label='Add Category')
if submit:
    add_category(name)

# view categories
if st.checkbox(label='View Categories'):
    for category in view_categories():
        st.info(f'{category.id} : {category.name}')

# add product
form2 = st.form(key='add_product')
name = form2.text_input(label='Product Name')
category = form2.text_input(label='Category ID')
submit = form2.form_submit_button(label='Add Product')
if submit:
    add_product(name, category)

# view products
if st.checkbox(label='View Products'):
    for product in view_products():
        st.info(f'{product.id} : {product.name}, {product.category}, {product.created_on.date()}')