## TINY language Scanner project (CSE-2019) Ain-Shams University

**How to use:**
1. download the **dist** folder from the repository.
2. place the code you want to scan in a text file and place it next to the exe file **main.exe**.
3. Drag and drop the text file on the exe file **OR** name your text file **sample_input.txt** and just double click the exe file.
4. A new file named **output.txt** will be created containing all the token with their types in the input file.

**Sample Input:**

```
{ Sample program in TINY language - computes factorial }
read x; {input an integer }
if 0 < x then { don't compute if x <= 0 }
fact := 1;
repeat
fact := fact * x;
x := x - 1
until x = 0;
write fact { output factorial of x }
end
```

**Sample Output:**

```
Type                 Token
=====                =====
COMMENT       { Sample program in TINY language - computes factorial }
READ                  read
IDENTIFIER               x
SEMICOLON                ;
COMMENT       {input an integer }
IF                      if
NUMBER                   0
LESS                     <
IDENTIFIER               x
THEN                  then
COMMENT       { don't compute if x <= 0 }
IDENTIFIER            fact
ASSIGNMENT              :=
NUMBER                   1
SEMICOLON                ;
IDENTIFIER      repeatfact
ASSIGNMENT              :=
IDENTIFIER            fact
MULT                     *
IDENTIFIER               x
SEMICOLON                ;
IDENTIFIER               x
ASSIGNMENT              :=
IDENTIFIER               x
MINUS                    -
NUMBER                   1
UNTIL                until
IDENTIFIER               x
EQUALS                   =
NUMBER                   0
SEMICOLON                ;
WRITE                write
IDENTIFIER            fact
COMMENT       { output factorial of x }
END                    end
```
