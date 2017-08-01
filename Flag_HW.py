import sys

def line_a():
    for i in range(0,6):
        sys.stdout.write("* ")
    for j in range(0,30):
        sys.stdout.write('=')
    sys.stdout.write('\n')

def line_b():
    for i in range(0,5):
        sys.stdout.write(" *")
    sys.stdout.write("  ")
    for i in range(0,30):
        sys.stdout.write('=')
    sys.stdout.write('\n')
    
def line_c():
    for i in range(0,42):
        sys.stdout.write('=')
    sys.stdout.write('\n')


def print_lines():
    for i in range(0,4):
        line_a()
        line_b()
    line_a()
    for j in range(0,5):
        line_c()
        
print_lines()

    