import sys, logging
from gnebehay_parser import parse
from argparse import ArgumentParser

_node_counter = 1

def _label(node):
    global _node_counter
    node.id = _node_counter
    _node_counter += 1
    for child in node.children:
        _label(child)

def _to_graphviz(node):
    print('graph ""')
    print('{')

    __to_graphviz(node)

    print('}')

def __to_graphviz(node):
    print('n{} [label="{}"] ;'.format(node.id, node.value))
    for child in node.children:
        print('n{} -- n{} ;'.format(node.id, child.id))
        __to_graphviz(child)

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
    ast = parse( args.input )
    _label( ast )
    _to_graphviz( ast )
