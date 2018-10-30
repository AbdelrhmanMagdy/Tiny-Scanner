import re
class scanner():
    other = False
    STATES = {        
        'START': True,
        'IN_COMMENT' : False,
        'IN_IDENTIFIER': False,
        'IN_NUMBER': False,
        'IN_ASSIGNMENT': False,
        'DONE': False,
        'OTHER': False
    }
    tokens = []
    KEYWORDS = ['else', 'end', 'if', 'repeat', 'then', 'until', 'read', 'write']
    OPERATORS = {
        '+'         : 'PLUS',
        '-'         : 'MINUS',
        '*'         : 'MULT',
        '/'         : 'DIV_FLOAT',
        ':'         : 'COLON',
        '='         : 'EQUALS',
        ':='        : 'ASSIGNMENT',
        '>'         : 'GREATER',
        '<'         : 'LESS',
        ';'         : 'SEMICOLON',
        '('         : 'OPEN_PARENTHESIS',
        ')'         : 'CLOSE_PARENTHESIS'
    }
    def set_state(self, state):
        for key in self.STATES:
            self.STATES[key] = False
        self.STATES[state] = True
    def get_state(self, state):
        return self.STATES[state]

    def print_state(self):
        for key,val in self.STATES.items():
            if val:
                print("state is " + key)

    def scan(self, str):
        token = ''
        for c in str:
            
            if self.get_state('START'):
                if self.is_symbol(c):
                    self.set_state('DONE')            
                elif c == ' ':
                    self.set_state('START')
                    continue
                elif c == '{':
                    self.set_state('IN_COMMENT')
                elif self.is_num(c):
                    self.set_state('IN_NUMBER')
                elif self.is_str(c):
                    self.set_state('IN_IDENTIFIER')
                elif self.is_col(c):
                    self.set_state('IN_ASSIGNMENT')
                
            elif self.get_state('IN_COMMENT'):
                if c == '}':
                    self.set_state('DONE')
                else:
                    self.set_state('IN_COMMENT')
            
            elif self.get_state('IN_NUMBER'):
                if self.is_num(c):
                    self.set_state('IN_NUMBER')
                elif c == ' ':
                    self.set_state('DONE')
                else:
                    self.set_state('OTHER')

            elif self.get_state('IN_IDENTIFIER'):
                if self.is_str(c):
                    self.set_state('IN_IDENTIFIER')
                elif c == ' ':
                    self.set_state('DONE')
                else:
                    self.set_state('OTHER')

            elif self.get_state('IN_ASSIGNMENT'):
                if c == '=':
                    self.set_state('DONE')
                else:
                    self.set_state('OTHER')

            if not self.get_state('OTHER'):
                token += c
            
            if self.get_state('OTHER'):
                self.set_state('DONE')
                self.other = True  

            if self.get_state('DONE'):
                self.classify(token)
                if self.other:
                    token = c
                    if self.is_col(c): self.set_state('IN_ASSIGNMENT')
                    if self.is_comment(c): self.set_state('IN_COMMENT')
                    if self.is_num(c): self.set_state('IN_NUMBER')
                    if self.is_str(c): self.set_state('IN_IDENTIFIER')
                    if self.is_symbol(c):
                        self.classify(c)
                        token = ''
                        self.set_state('START')
                    self.other = False
                else:
                    token = ''
                self.set_state('START')

    def classify(self, token):
        if token[-1:] == ' ': token = token[0:-1]
        if self.is_str(token):
            if token in self.KEYWORDS:
                self.tokens.append([token, token.upper()])
            else:
                self.tokens.append([token , 'IDENTIFIER'])
        elif self.is_num(token):
            self.tokens.append([token, 'NUMBER'])
        elif token in self.OPERATORS:
            self.tokens.append([token, self.OPERATORS[token]])
        elif self.is_comment(token):
            self.tokens.append([token, 'COMMENT'])
            
    def is_str(self, token):
        return token.isalpha()
    def is_num(self, token):
        return token.isdigit()
    def is_col(self, c):
        return True if c == ':' else False
    def is_symbol(self, token):
        symbol = ['+', '-', '*', '/', '=', '<', '>', '(', ')', ';']
        return True if token in symbol else False
    def is_comment(self, token):
        return True if re.match(r'^{.+}$', token) else False


input_file  = open('input.txt', 'r')
input_text = input_file.read()

x = scanner()
x.scan(input_text.replace('\n', ' '))
output_file = open('output.txt','w')

for t in x.tokens:
    output_file.write(t[0] + ', ' + t[1] + '\n') 

input_file.close()
output_file.close() 