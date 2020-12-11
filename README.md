<h1> Rule format </h1>


A => B,  A inference B <br>
A + B => C, A and B inference C <br>
A | B => C, A or B inference C <br>
A ^ B => C, A xor B inference C <br>
A + !B => C, A and not B inference C <br>
! A => B, Not A infence B <br>
Example: <br>
A + B => C
C | E => D
B + ( C | E ) => G
=AB <br>
?D <br>

Symbols
---
"=>" Inference <br>
"+" And <br>
"|" Or <br>
"^" Xor <br>
"!" Not <br>
"?" Searched Queries (?AE) <br>
"=" Initial Facts (=ABC) <br>
"#" Comment

