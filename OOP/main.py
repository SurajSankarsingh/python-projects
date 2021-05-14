#OOP
class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('run')

player1  = PlayerCharacter('steve', 44)
player2  = PlayerCharacter('dave', 33)

print(player1.name, player1.age)
print(player2.name, player2.age)