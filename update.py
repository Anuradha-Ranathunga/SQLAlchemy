from main import Session, engine, User

try:
    local_session =Session(bind=engine)
    user_to_update= local_session.query(User).filter(User.username=="Jona").first()
    
    print(user_to_update)

    user_to_update.username= "jonathan"
    user_to_update.email = "jonathan@company.com"

    local_session.commit()
    local_session.refresh(user_to_update)
except Exception as e:
    print(e)
