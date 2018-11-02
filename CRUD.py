from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from Config import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create
myFirstRestaurant = Restaurant(name="Pizza Palace")

session.add(myFirstRestaurant)

session.commit()

# print(session.query(Restaurant).all())

cheesepizza = MenuItem(name="Cheese Pizza", description="MAde with all natural ingredients and fresh mozzarella",
                       course="Entree", price="$8.99", restaurant=myFirstRestaurant)

session.add(cheesepizza)

# print(session.query(MenuItem).all())

firstResult = session.query(Restaurant).first()

print(firstResult.name)

items = session.query(MenuItem).all()

# for item in items:
    # print(item.name)

# Filter one and update

veggie = session.query(MenuItem).filter_by(id=1).one()
print(veggie.price)

veggie.price = '$2.99'
session.add(veggie)
session.commit()

# Filter collection & update
urbanVeggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in urbanVeggieBurgers:
    if veggieBurger.restaurant.name == "Urban Burger":
        veggieBurger.price != '$2.99'
        veggieBurger.price = '$2.99'
        session.add(veggie)
        session.commit()
        # print(veggieBurger.id)
        # print(veggieBurger.price)
        # print(veggieBurger.restaurant.name)
        # print("\n")

# delete
spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream')
for span in spinach :
    print(span.restaurant.name)
    session.delete(span)
    session.commit()
