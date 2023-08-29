def main():
  print(
      "This program will create a .py file with basic setup. Dont give it a file extension"
  )
  name = input("File Name: ")
  name = name + ".py"
  makeFile(name)


def makeFile(name):
  f = open(name, "w")
  f.write("Setup will go here")


if __name__ == "main":
  main()