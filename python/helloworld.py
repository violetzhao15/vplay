#hello python3

print("hello pyhon3")

j = 1
i = 5
print(f"i={i}")
print("i=",i)
i = i+1
print(f"after i++; i={i}")

def print_max(a,b):
    print(f"a={a}, b={b}")
    if(a>b):
        print("max is", a)
    else:
        print("max is", b)

print_max(8,11)

def global_test():
    global i
    i = 11
    print(f"in global_test; i={i}")

global_test()

print(f"global i={i}")

def func_default_v_test(a, b=5, c=100):
    print("a=", a, "b=", b, "c=", c)
func_default_v_test(1)
func_default_v_test(1,2)
func_default_v_test(1,2,3)

class Person:
    def say_hi(self): #compile error if self was not given here
        print("hello, how are you")

    def gotoshcool(self, a):
    	print("my school is:", a)

p1 = Person()
print("p=",p1)
p1.say_hi()


p1.say_hi()

p1.gotoshcool("Bradfield")


class Person2:
	age=0
	height=170
	weight=60
	name="Bruce"

	def print_name(self):
		print("name is:", self.name)

p2 = Person2()
p2.print_name()


