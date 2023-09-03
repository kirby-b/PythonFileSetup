def main():
  print("This program will create a .py file with basic setup. Dont give it a file extension")
  name = input("File Name: ")
  name = name + ".py"
  makeFile(name)


def makeFile(name):
  f = open(name, "w")
  f.write("""def main():
    pass
def newFunc():
    pass
if __name__ == "__main__":
    main()""")


if __name__ == "__main__":
    main()