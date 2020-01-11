# class Parent(object):
#     def implicit(self):
#         print("PARENT implicit()")

# class Child(Parent):
#     pass

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# class Parent():
#     def override(self):
#         print("PARENT override()")

# class Child(Parent):
#     def over(self):
#         print("CHILD override()")

# dad = Parent()
# son = Child()

# dad.override()
# son.override()


# class Parent(object):
#     def alter(self):
#         print("PARENT altered()")

# class Child(Parent):
#     def abc(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).alter()
#         print("CHILD, AFTER PARENT altered()")

# dad = Parent()
# son = Child()

# dad.alter()
# son.abc()


class Parent(object):
    def override(self):
        print("PARENT override()")
    def implicit(self):
        print("PARENT implicit()")
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).implicit()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()

dad.implicit()
son.implicit()

dad.override()
son.override()

