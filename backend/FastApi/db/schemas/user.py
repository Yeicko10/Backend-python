def user_schema(user) -> dict:      #transformar el objeto de la base de datos a un objeto de python
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}


def users_schema(users) -> list:
    return [user_schema(user) for user in users]
