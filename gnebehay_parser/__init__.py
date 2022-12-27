import enum, re, logging
from itertools import chain

class TokenType(enum.Enum):
    T_NUM = 0
    T_PLUS = 1
    T_MINUS = 2
    T_MULT = 3
    T_DIV = 4
    T_LPAR = 5
    T_RPAR = 6
    T_VAR  = 7
    T_EXP  = 8
    T_END = 9


_mappings = {
    '+': TokenType.T_PLUS,
    '-': TokenType.T_MINUS,
    '*': TokenType.T_MULT,
    '/': TokenType.T_DIV,
    '^': TokenType.T_EXP,
    '(': TokenType.T_LPAR,
    ')': TokenType.T_RPAR}

def _isint( tok ):
    try:
        val = int( tok )
        return True
    except:
        return False

    
class Node( object ):
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []
    
    def __str__( self ):
        return '%s, %s, num_child = %d' % (
            self.token_type, self.value, len( self.children ) )

def _get_token_mapping( tok ):
    if tok in _mappings:
        token_type = _mappings[ tok ]
        return Node(token_type, value = tok )
    #
    if _isint( tok ):
        return Node(TokenType.T_NUM, value=int(tok))
    #
    if isinstance( tok, str ):
        return Node(TokenType.T_VAR, tok )
    raise Exception('Invalid token: {}'.format( tok ) )

def lexical_analysis(s):
    splitstring = s.strip( ).replace('(', ' ( ' ).replace(')', ' ) ' ).strip( ).split( )
    logging.debug( 'init splitstring = %s.' % splitstring )
    splitstring = list( chain.from_iterable(
        map(lambda tok:
            filter(lambda elem: len(elem) > 0,
                   re.split(r'(\d+|\W+)', tok.strip())), splitstring)))
    logging.debug( 'final splitstring = %s.' % splitstring )
    #
    tokens = list(map(
        _get_token_mapping, splitstring ) )
    #
    tokens.append(Node(TokenType.T_END))
    return tokens


def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise Exception('Invalid syntax on token {}'.format(tokens[0].token_type))

def parse_e(tokens):
    left_node = parse_e2(tokens)
    while tokens[0].token_type in [TokenType.T_PLUS, TokenType.T_MINUS]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e2(tokens))
        left_node = node
    return left_node

def parse_e2(tokens):
    left_node = parse_e3(tokens)
    while tokens[0].token_type in [TokenType.T_MULT, TokenType.T_DIV]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e3(tokens))
        left_node = node
    return left_node


def parse_e3( tokens ):
    left_node = parse_e4(tokens)
    while tokens[0].token_type in [TokenType.T_EXP, ]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e4(tokens))
        left_node = node
    return left_node

def parse_e4(tokens):
    if tokens[0].token_type == TokenType.T_NUM:
        return tokens.pop(0)
    if tokens[0].token_type == TokenType.T_VAR:
        return tokens.pop( 0 )
    match(tokens, TokenType.T_LPAR)
    expression = parse_e(tokens)
    match(tokens, TokenType.T_RPAR)
    return expression

def parse(inputstring):
    tokens = lexical_analysis(inputstring)
    ast = parse_e(tokens)
    match(tokens, TokenType.T_END)
    return ast
