FILEPATH = "todos1.txt"
import os

if not os.path.exists(FILEPATH):
    with open(FILEPATH,'w'):
        pass


def get_todos(filepath=FILEPATH):
    """This function or routine is used to read the todos from the
    FILEPATH and return it"""
    with open(filepath) as file:
        todos_local = file.readlines()
    return todos_local

def set_todos(todos_arg,filepath=FILEPATH):
    """This function or routine is used to write the todos list
    supplied to the file mentioned in FILEPATH"""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

if __name__=="__main__":
    print(get_todos())
    help(get_todos)
    help(set_todos)