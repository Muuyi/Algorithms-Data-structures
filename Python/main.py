# This is a sample Python script.
print(2**(3**2),(2**3)**2,(2**3)**3)
def f(x,l=[]):
    for i in range(x):
        l.append(i*1)
    print(l)
f(2)
f(3,[3,2,1])
f(3)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# class Welcome:
#     def __init__(self,name):
#         self.name = name
#     def say_hello(self):
#         print("Welcome to", self.name)
# cw = Welcome('Turing')
# cw.say_hello()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t = '%(a)s'
    print(t % dict(a='Welcome'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
