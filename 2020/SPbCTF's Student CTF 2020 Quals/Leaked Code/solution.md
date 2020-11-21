# Leaked Code writeup

Сразу замечаем, что предоставленный в таске файл `leaked` является текстовым представлением `Java` байт-кода:

```java
DEFINE PUBLIC STATIC main([Ljava/lang/String; args)V
A:
LINE A 7
GETSTATIC java/lang/System.out Ljava/io/PrintStream;
LDC "Enter access code : "
INVOKEVIRTUAL java/io/PrintStream.print(Ljava/lang/String;)V
B:
LINE B 8
NEW java/util/Scanner
DUP
GETSTATIC java/lang/System.in Ljava/io/InputStream;
INVOKESPECIAL java/util/Scanner.<init>(Ljava/io/InputStream;)V
ASTORE scanner
C:
LINE C 9
ALOAD scanner
INVOKEVIRTUAL java/util/Scanner.nextLine()Ljava/lang/String;
ASTORE access_code
D:
LINE D 10
LDC "abcdefghijklmnopqrstuvwxyz_!@"
ASTORE alphabet
E:
LINE E 11
ALOAD access_code
INVOKEVIRTUAL java/lang/String.length()I
BIPUSH 24
IF_ICMPEQ H
F:
LINE F 12
GETSTATIC java/lang/System.out Ljava/io/PrintStream;
LDC "Nope!"
INVOKEVIRTUAL java/io/PrintStream.println(Ljava/lang/String;)V
G:
LINE G 13
RETURN
H:
LINE H 15
ALOAD access_code
LDC "spbctf{"
INVOKEVIRTUAL java/lang/String.startsWith(Ljava/lang/String;)Z
IFEQ I
ALOAD access_code
ALOAD access_code
INVOKEVIRTUAL java/lang/String.length()I
ICONST_1
ISUB
INVOKEVIRTUAL java/lang/String.codePointAt(I)I
BIPUSH 125
IF_ICMPEQ K
I:
LINE I 16
GETSTATIC java/lang/System.out Ljava/io/PrintStream;
LDC "Nope!"
INVOKEVIRTUAL java/io/PrintStream.println(Ljava/lang/String;)V
J:
LINE J 17
RETURN
K:
LINE K 19
ICONST_5
ISTORE seed
L:
LINE L 20
BIPUSH 7
ISTORE i
M:
ILOAD i
BIPUSH 23
IF_ICMPGE S
N:
LINE N 21
ALOAD access_code
ILOAD i
INVOKEVIRTUAL java/lang/String.codePointAt(I)I
ALOAD alphabet
ILOAD seed
INVOKEVIRTUAL java/lang/String.codePointAt(I)I
IF_ICMPEQ Q
O:
LINE O 22
GETSTATIC java/lang/System.out Ljava/io/PrintStream;
LDC "Nope!"
INVOKEVIRTUAL java/io/PrintStream.println(Ljava/lang/String;)V
P:
LINE P 23
RETURN
Q:
LINE Q 25
ILOAD seed
ICONST_3
IMUL
ALOAD alphabet
INVOKEVIRTUAL java/lang/String.length()I
IREM
ISTORE seed
R:
LINE R 20
IINC i 1
GOTO M
S:
LINE S 27
GETSTATIC java/lang/System.out Ljava/io/PrintStream;
LDC "Access granted!"
INVOKEVIRTUAL java/io/PrintStream.println(Ljava/lang/String;)V
T:
LINE T 28
RETURN
U:
```

Воспользуемся [этой статьёй из Википедии](https://en.wikipedia.org/wiki/Java_bytecode_instruction_listings) для перевода инструкций байт-кода в программный код на `Java` и 
получим следующий скрипт:

```java
import java.util.*;

public class leaked {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter access code : ");
        String access_code = scanner.next();
        String alphabet = "abcdefghijklmnopqrstuvwxyz_!@";
        if (access_code.length() == 24) {
           if (access_code.startsWith("spbctf{") == false) {
              System.out.println("Nope!");
           }
           if (access_code.codePointAt(access_code.length() - 1) == 125) {
              int seed = 5;
              int i = 7;
              if (i >= 23) {
                 System.out.println("Access granted!");
              }
              if (alphabet.codePointAt(seed) == access_code.codePointAt(i)) {
                 seed = (seed * 3) % alphabet.length();
              }
              i++;
           }
        }
    }
}
```

Теперь осталось написать скрипт, который выведет искомую строку:

```python3
alphabet = 'abcdefghijklmnopqrstuvwxyz_!@'
flag = 'spbctf{'
seed = 5

for i in range(7, 23):
    flag += alphabet[seed]
    seed = (seed * 3) % len(alphabet)

flag += '}'
print(flag)
```

Flag: `spbctf{fpqt@_ucgszrwiyo}`
