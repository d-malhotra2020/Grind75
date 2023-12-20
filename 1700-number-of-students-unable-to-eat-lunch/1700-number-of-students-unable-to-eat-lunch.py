class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        SandwichCounter = 0
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                SandwichCounter = 0
            else:
                student = students.pop(0)
                students.append(student)
                SandwichCounter +=1
                if SandwichCounter == len(students):
                    break
        return len(students)