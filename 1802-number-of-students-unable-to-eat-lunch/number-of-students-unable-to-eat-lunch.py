class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwichcounter = 0
        while sandwiches and students:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                sandwichcounter = 0
            else:
                student = students.pop(0)
                students.append(student)
                sandwichcounter +=1
                if sandwichcounter == len(students):
                    break
        return len(students)