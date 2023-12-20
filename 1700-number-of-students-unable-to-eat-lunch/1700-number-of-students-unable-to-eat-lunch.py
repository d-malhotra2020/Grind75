class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwichCounter = 0
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                sandwichCounter = 0
            else:
                student = students.pop(0)
                students.append(student)
                sandwichCounter +=1
                if sandwichCounter == len(students):
                    break
        return len(students)