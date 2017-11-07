class Animal(object):
	def __init__(self,Type,sound,name,age,color):
		self.type = Type
		self.sound = sound
		self.name = name
		self.age = age
		self.color = color
	def eat(self,food):
		print("yummy! " + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is a " + self.type + " and its " + self.age + " years old and its favorite color is " + self.color)
	def MakeSound(self,x):
			print(self.sound + " ")*x

cat = Animal("cat","meow", "lele", "2", "white")

cat.description()
cat.eat("wiskis")
cat.MakeSound(5)
class Person(object):
	def __init__(self,name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender

	def Eat(self, food):
		print(self.name + "is enjoing his " + food)

Jack = Person("Jack ", 18, "Jerusalem", "Male")
Jack.Eat("omlet")

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def SingTheSong(self):
		for value in self.lyrics:
			print(value)


flowrs = Song(["roses are red","violets are blue","i wrote this poem just for you"])


flowrs.SingTheSong()





