import ast

expr="2 * (3 -1) + 2 * 5"
node = ast.parse(expr, mode='eval')
print(ast.dump(node).replace(',', ',\n'))
code_object = compile(node, filename='<string>', mode='eval')
print(eval(code_object))
print(node.body.right.right.n)
node.body.right.right.n = 6
code_object = compile(node, filename='<string>', mode='eval')
print(eval(code_object))
