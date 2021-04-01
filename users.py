def login(username,password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            return True
        else:
            return False
#funktio antaa joko käyttäjän id-numeron tai arvon 0, jos käyttäjä ei ole kirjautunut sisään
def user_id():
    return session.get("user_id",0)
#kirj.ulos istunnosta
def logout():
    del session["user_id"]
# uuden käyttäjän rekisteröiminen sovellukseen
def register(username,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username,password)
