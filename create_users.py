from main import User, Session,engine

users = [
{
    "username": "jerry",
    "email": "jerry@company.com"
},
  {
    "username": "jordan",
    "email": "jordan@company.com" 
},{
    "username": "jackson",
    "email": "jackson@company.com" 
},{
    "username": "john",
    "email": "john@company.com"
},{
    "username": "jack",
    "email": "jack@company.com"
}
         
]

local_session = Session(bind=engine)

#new_user = User(username = "Jona", email="jona@company.com")

#local_session.add(new_user)
#local_session.commit()

for u in users:
    new_user = User(username =u["username"] , email=u["email"])
    
    #print(new_user)
    
    local_session.add(new_user)
    local_session.commit()
    print(f"Added{u['username']}")
