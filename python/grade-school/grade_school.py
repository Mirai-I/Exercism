class School:
    def __init__(self):
        self.student = []

    def add_student(self, name, grade):
        #　新しい学生情報を追加
        self.student.append((grade,name))
        self.student.sort()

    def roster(self):
        return  [i[1] for i in self.student]

    def grade(self, grade_number:int):
        return [i[1] for i in self.student if i[0] == grade_number]
