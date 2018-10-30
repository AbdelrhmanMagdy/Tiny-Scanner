from scanner import scanner

def main():
    obj = scanner()
    obj.scan('input.txt')
    obj.output()

if __name__ == "__main__":
    main()