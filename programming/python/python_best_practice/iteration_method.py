"""
# Bad
# Can't change type of collection
#     e.g. can't change employees from a list to a set
class Department:
    def __init__(self, *employees):
        self.employees = employees

for employee in department.employees:
    ...
    
# Better
class Department:
    def __init__(self, *employees):
        self._employees = employees

    def __iter__(self):
        return iter(self._employees)

for employee in department:  # More readable, more composable
    ...

https://stevenloria.com/python-best-practice/
https://gist.github.com/sloria/5895749#file-gistfile1-py
"""

class Department:

    def __init__(self, employees):
        self._employees = employees

    def __iter__(self):
        return iter(self._employees)

department = Department([1, 2, 3])
for emp in department:
    print(emp)

