import re
class scanner():

    def __init__(self):
        self.set_state('START')
        self.tokens = []
        self.state_other = False

    def set_state(self, state):
        for key in self.STATES:
            self.STATES[key] = False
        self.STATES[state] = True

    def get_state(self, state):
        return self.STATES[state]

    def scan(self, input_file='input.txt'):
        input_text = self.read_file(input_file)
        token = ''
        for c in input_text:
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
                self.state_other = True  

            if self.get_state('DONE'):
                self.classify(token)
                if self.state_other:
                    token = c
                    if self.is_col(c): self.set_state('IN_ASSIGNMENT')
                    if self.is_comment(c): self.set_state('IN_COMMENT')
                    if self.is_num(c): self.set_state('IN_NUMBER')
                    if self.is_str(c): self.set_state('IN_IDENTIFIER')
                    if self.is_symbol(c):
                        self.classify(c)
                        token = ''
                        self.set_state('START')
                    self.state_other = False
                else:
                    token = ''
                self.set_state('START')

    def classify(self, token):
        print(token)
        if token[-1:] == ' ': token = token[0:-1]
        token = token.replace('\n','')
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

    def read_file(self, fileName):
        with open(fileName, 'r') as f:
            input_text = f.read()
            return input_text

    def output(self):
        with open('output.txt', 'w') as f:
            f.write('{:<12}  {:>12}\n'.format('Type', 'Token'))
            f.write('{:<12}  {:>12}\n'.format('=====', '====='))
            for token in self.tokens:
                f.write('{:<12}  {:>12}\n'.format(token[1], token[0]))
    
    
    STATES = {        
        'START': False,
        'IN_COMMENT' : False,
        'IN_IDENTIFIER': False,
        'IN_NUMBER': False,
        'IN_ASSIGNMENT': False,
        'DONE': False,
        'OTHER': False
    }
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
