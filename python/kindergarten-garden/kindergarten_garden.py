import re

class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie",
    "David","Eve", "Fred","Ginny",
    "Harriet","Ileana", "Joseph",
    "Kincaid","Larry"]):
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, name:str) -> list:
        diagram= who(self)
        numbre = self.students.index(name)
        return diagram[numbre]

def who(self):
    plants = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}
    each_plant = self.diagram.splitlines()
    len_each_plant = max(len(each_plant[0]),len(each_plant[1]))

    new_plants_name = [[each_plant[0][i],each_plant[0][i+1],each_plant[1][i],each_plant[1][i+1]] for i in range(0, len_each_plant-1, 2)]
    new_diagram = []
    for p in new_plants_name:
        new_diagram += [[plants[pp] for pp in p]]

    return new_diagram
