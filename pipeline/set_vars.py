import os

def set_vars():
    with open('.env', 'r') as f:
        vars = f.read()
    vars = vars.split('\n')
    os.environ['USER_NAME'] = vars[0]
    os.environ['PASSWORD'] = vars[1]

if __name__ == "__main__":
    set_vars()