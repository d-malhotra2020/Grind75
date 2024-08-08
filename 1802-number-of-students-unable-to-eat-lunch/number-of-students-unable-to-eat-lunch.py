class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        NumberOfSandwiches = 0
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                NumberOfSandwiches = 0
            else:
                student = students.pop(0)
                students.append(student)
                NumberOfSandwiches +=1
                if NumberOfSandwiches == len(students):
                    break
        return len(students)