from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "Max Nguyen"


max_nguyen = User(id=111)

assert max_nguyen.id == 111
assert isinstance(max_nguyen.id, int)
assert max_nguyen.__fields_set__ == {"id"}

# Fields were supplied when user was initialised
assert max_nguyen.dict() == dict(max_nguyen) == {"id": 111, "name": "Max Nguyen"}


print(max_nguyen.json())
