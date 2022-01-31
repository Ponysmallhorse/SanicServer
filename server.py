from sanic import Sanic
from sanic.response import json
from sanic_jwt import exceptions, Initialize
from sanic_jwt.decorators import protected

app = Sanic("NormalizeApp")


class User:

    def __init__(self, id, username, password):
        self.user_id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "User(id='{}')".format(self.user_id)

    def to_dict(self):
        return {"user_id": self.user_id, "username": self.username}


users = [User(1, "test", "test"), User(2, "user2", "abcxyz")]

username_table = {u.username: u for u in users}


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = username_table.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user


@app.post("/normalize")
@protected()
def normalize(request):
    request_json = request.json
    response_json = {obj["name"]: [obj[val] for val in obj if val.endswith("Val")][0] for obj in request_json}
    return json(response_json)


Initialize(app, authenticate=authenticate)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)
