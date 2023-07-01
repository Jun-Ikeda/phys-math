class MathNodeType:
    name = ''
    domain = None
    codomain = None
    func = None
    str_func = None

    def __init__(self, name, domain, codomain, func, str_func):
        self.name = name
        self.domain = domain
        self.codomain = codomain
        self.func = func
        self.str_func = str_func

    def __str__(self):
        return self.str_func()
    
class MathNode:
    type = None
    children = None

    def __init__(self, type, children):
        self.type = type
        if type.domain is not None:
            for domain, child in zip(type.domain, children):
                if domain != child.type.codomain:
                    raise TypeError(f'Expected {domain}, got {child.type.codomain}')
        self.children = children

    def __str__(self):
        if self.type.name == 'symbol':
            return f'{self.type.str_func(*self.children)}'
        else:
            return f'({self.type.str_func(*self.children)})'
    
    def value(self):
        return self.type.func(*self.params)