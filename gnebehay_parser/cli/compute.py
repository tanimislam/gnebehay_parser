import sys, operator, logging
from gnebehay_parser import parse, TokenType
from argparse import ArgumentParser

_operations = {
    TokenType.T_PLUS: operator.add,
    TokenType.T_MINUS: operator.sub,
    TokenType.T_MULT: operator.mul,
    TokenType.T_DIV: operator.truediv,
    TokenType.T_EXP: operator.pow
}

def _compute( node ):
    if node.token_type == TokenType.T_NUM:
        return node.value
    left_result = _compute(node.children[0])
    right_result = _compute(node.children[1])
    operation = _operations[node.token_type]
    return operation(left_result, right_result)

def main( ):
    parser = ArgumentParser( )
    parser.add_argument( '-i', '--input', dest = 'input', type = str, required = True,
                        help = 'The arithmetic expression to compute.' )
    parser.add_argument( '-D', '--debug', dest = 'do_debug', action = 'store_true', default = False,
                        help = 'If chosen, then turn on DEBUG logging. Useful to figure out what went wrong.' )
    #
    args = parser.parse_args( )
    #
    logger = logging.getLogger( )
    if args.do_debug: logger.setLevel( logging.DEBUG )
    #
    ast = parse( args.input.strip( ) )
    result = _compute(ast)
    print(result)
