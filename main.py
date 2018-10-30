from scanner import scanner
import sys

def main():
    file_name = sys.argv[1] if len(sys.argv)>1 else 'sample_input.txt'
    obj = scanner()
    obj.scan(file_name)
    obj.output()

if __name__ == "__main__":
    main()