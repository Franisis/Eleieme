#########################################

#########################################
#TOKEN CONSTANTS
TT_IF = "TT_IF"
TT_NOT = "TT_NOT"
TT_BLOCKED = "TT_BLOCKED"
TT_WALK = "TT_WALK"
TT_ROTATE = "TT_ROTATE"
TT_DEFINE = "TT_DEFINE"
TT_FOO = "TT_FOO"
TT_NOP = 'TT_NOP'
TT_LEFT = 'TT_LEFT'
TT_RIGHT = 'TT_RIGHT'
TT_BACK = 'TT_BACK'
TT_FREE = 'TT_FREE'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'
TT_DROP = "TT_DROP"
TT_PROC = "TT_PROC"
TT_GO = "TT_GO"
TT_PUT = "TT_PUT"
TT_GORP = "TT_GORP"
TT_LOOK = "TT_LOOK"
TT_GRAB = "TT_GRAB"
TT_JUMP = "TT_JUMP"
TT_JUMPTO = "TT_JUMPTO"
TT_VEER = "TT_VEER"
TT_GET = "TT_GET"
TT_POP = "TT_POP"
TT_CANWALK = "TT_CANWALK"
TT_RIGHTCOR = "TT_RIGHTCOR"
TT_LEFTCOR = "TT_LEFTCOR"
TT_EQUALS = "TT_EQUALS"
TT_DO = "TT_DO"
TT_GORP = "TT_GORP"
TT_VAR = "TT_VAR"
#########################################
alfabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#########################################

class Token:
    def __init__(self, type_, value_) -> None:
        self.type = type_
        self.value = value_

    def __repr__(self) -> str:
        if self.value: 
            return f'{self.type}:{self.value}'
        return f'{self.type}'
        

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = -1
        self.advance()

    def advance(self):
        self.pos+=1
        self.current_char = self.text[self.pos] if self.pos < len (self.text) else None

    def make_tokens(self):
        tokens = []
        word = ''
        while self.current_char !=None:
            if self.current_char in '\t':
                self.advance()
            elif self.current_char == "r" and word == "":
                word+="r"
                self.advance()
            elif self.current_char == "i" and word == "r":
                word+="i"
                self.advance()
            elif self.current_char == "g" and word == "ri":
                word+="g"
                self.advance()
            elif self.current_char == "h" and word == "rig":
                word+="h"
                self.advance()
            elif self.current_char == "t" and word == "righ":
                word+="t"
                self.advance()
            
            if self.current_char == 'l':
                word+='l'
                self.advance()
            elif self.current_char == 'e' and word == "l":
                word+='e'
                self.advance()
            elif self.current_char == 'f' and word == "le":
                word+='f'
                self.advance()
            elif self.current_char == 't' and word == "lef":
                word+='t'
                self.advance()

            if self.current_char == 'v':
                word+=self.current_char
                self.advance()
            elif self.current_char == 'a' and word == "v":
                word+=self.current_char
                self.advance()
            elif self.current_char == "r" and word == "va":
                word+=self.current_char
                self.advance()

            if word == 'right':
                tokens.append(TT_RIGHT)
                word=''
            elif word == 'left':
                tokens.append(TT_LEFT)
                word =''
            elif word == 'var':
                tokens.append(TT_VAR)
                word =''
            elif word == "GORP":
                tokens.append(TT_GORP)
                break
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'"+ char + "'")

            return tokens
        

    def make_vars(self):
        var_str = ''
        dot_count=0
        while self.current_char != None and self.current_char in alfabet:
            var_str += self.current_char()



class Error:
    def __init__(self,error_name,details)    :
        self.error_name = error_name
        self.details = details
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result
class IllegalCharError(Error):
    def __init__(self,details):
        super().__init__('Illegal Character', details)
########################
#RUN
########################
def run(text):
    lexer = Lexer(text)
    tokens , error = lexer.make_tokens()
    return tokens, error


