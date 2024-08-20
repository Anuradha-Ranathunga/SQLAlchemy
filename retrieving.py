from main import User, Session, engine


local_session = Session(bind=engine)

#return all objects
#users= local_session.query(User).all()[:3]

#for user in users:
#    print(user.username)

#query for one object
jona = local_session.query(User).filter(User.username=="Jona").first()

print(jona.username)    
