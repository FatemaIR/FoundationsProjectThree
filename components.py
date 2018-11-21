# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age




class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.group = []


    def assign_president(self, person):
        # your code goes here!
        self.group.append(person)


    def recruit_member(self, person):
        # your code goes here!
        self.group.append(person)


    def print_member_list(self):
        # your code goes here!
        num_of_members = 0
        members_ages = 0
        for person in self.group:
            print( person.name + "(" + str(person.age) + " years old) - " + person.bio)
            print()
            num_of_members = num_of_members + 1
            members_ages = members_ages + person.age
        average = float(members_ages) / num_of_members

        print("\nAverage of ages in this club is: %f years. \n" % average)
        print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
        

            

