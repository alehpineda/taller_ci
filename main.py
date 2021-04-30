def suma(x, y):
    if type(x) == int and type(y) == int:
        return x + y
    else:
        raise TypeError


def resta(x, y):
    return x - y


def division(x, y):
    if x == 0 or y == 0:
        raise ZeroDivisionError
    return x / y


cadena = """a;sdljkha;lkdsjf;lkajsd;lkn;lakns;
            ldknv;lakns;dlknf;lkasnd;lkfna;
            lksdn;lkvna;lksndvf"""
