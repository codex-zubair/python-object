
class abc:
  def __init__(self):
    print("abc")



class be(abc):
    print("be");


class me(abc):
    print("me");


class an(be):
    print("be");

class mo(be):
    print("mo");

class me (abc):
    print("me");

class k(abc):
    print("K");



print(abc());