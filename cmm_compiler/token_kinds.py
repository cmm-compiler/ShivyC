"""The token kinds currently recognized.

Tokens Supported:
Keywords: int|void|if|else|while|return
Identifier: [a-zA-Z]([a-zA-Z]|\d)*
Numbers: [1-9][0-9]*
Assignment: =
Calculate Token: +|-|*|/|=|==|>|>=|<|<=|!=
Division Token: ;
Partition Token: ,
Notation Token: /* */ | //
Left Parenthese: (
Right Parenthese: )
Left Bracket: {
Right Bracket: }
Alphabets: [a-zA-Z]
Numbers: [0-9]
End Token: #
"""

from cmm_compiler.tokens import TokenKind

keyword_kinds = []
symbol_kinds = []

int_kw = TokenKind("int", keyword_kinds)
void_kw = TokenKind("void", keyword_kinds)
if_kw = TokenKind("if", keyword_kinds)
else_kw = TokenKind("else", keyword_kinds)
while_kw = TokenKind("while", keyword_kinds)
return_kw = TokenKind("return", keyword_kinds)

plus = TokenKind("+", symbol_kinds)
minus = TokenKind("-", symbol_kinds)
star = TokenKind("*", symbol_kinds)
slash = TokenKind("/", symbol_kinds)
equals = TokenKind("=", symbol_kinds)
twoequals = TokenKind("==", symbol_kinds)
gt = TokenKind(">", symbol_kinds)
gtoe = TokenKind(">=", symbol_kinds)
lt = TokenKind("<", symbol_kinds)
ltoe = TokenKind("<=", symbol_kinds)
notequal = TokenKind("!=", symbol_kinds)

semicolon = TokenKind(";", symbol_kinds)

comma = TokenKind(",", symbol_kinds)

slash_star = TokenKind("/*", symbol_kinds)
star_slash = TokenKind("*/", symbol_kinds)
slash_slash = TokenKind("//", symbol_kinds)

open_paren = TokenKind("(", symbol_kinds)
close_paren = TokenKind(")", symbol_kinds)
open_brack = TokenKind("{", symbol_kinds)
close_brack = TokenKind("}", symbol_kinds)

identifier = TokenKind()
number = TokenKind()
string = TokenKind()
char_string = TokenKind()
include_file = TokenKind()
