class conjunto:
    def __init__(self,a,b,c):
        u = universo()
        v = True

        for e in a:
            if len(e) != 1 or e.isnumeric:
                v = False
                break
        if v:
            c[b] = a
            u.getinstancia().datos |= a
class universo(conjunto):
    instancia = None
    datos = set()
    @staticmethod
    def getinstancia():
        if universo.instancia == None:
            universo()
        return universo.instancia
    def __init__(self):
        universo.instancia = self
dic = dict()

def operacion(a):

    if "n" in a:
        if (a.index("n") != 0 and a[ a.index("n") -1] not in ["u","n","-","!"]) and (a.index("n") != len(a)-1 and a[ a.index("n") -1] not in ["u","n","-","!"]):
            return operacion(a[0:a.index("n")]) & operacion(a[a.index("n") + 1::])
        else:
            f[0] = False
            return set()
    elif "u" in a:
        if (a.index("n") != 0 and a[a.index("n") - 1] not in ["u", "n", "-", "!"]) and (
                a.index("n") != len(a) - 1 and a[a.index("n") - 1] not in ["u", "n", "-", "!"]):
            return operacion(a[0:a.index("n")]) | operacion(a[a.index("n") + 1::])
        else:
            f[0] = False
            return set()
    elif "-" in a:
        if (a.index("n") != 0 and a[a.index("n") - 1] not in ["u", "n", "-", "!"]) and (
                a.index("n") != len(a) - 1 and a[a.index("n") - 1] not in ["u", "n", "-", "!"]):
            return operacion(a[0:a.index("n")]) & operacion(a[a.index("n") + 1::])
        else:
            f[0] = False
            return set()
    else:
        if "!" in a:
            if len(a) == 2:
                return u.getinstancia().datos - dic[a[1]]
            else:
                f[0] = False
                return set()
        else:
            if len(a) == 1 and a in dic.keys():
                return dic[a]
            else:
                f[0] = False
                return set()

u = universo()
while True:
    f = [True]
    esta = input().replace(" ","")
    if len(esta) > 1 and esta[1] == "=":
        conjunto(set(esta[3:-1].split(",")),esta[0],dic)
    else:
        n = 0
        op = esta
        #que aya el mismo numero de ( y de )

        if esta.count("(") == esta.count(")"):
            while ")" in op:
                a = op[op.index(")") - op[0:op.index(")")][::-1].index("("):op.index(")")]
                dic[str(n)] = operacion(a)
                op = op.replace("(" + a + ")", str(n))
                n += 1
            if f[0]:
                print(operacion(op))
'''dic['a'] = {1,2,4,5}
dic['b'] = {2,3,5,6}
dic['c'] = {4,5,6,7}
universo = {1,2,3,4,5,6,7}'''
print("aqui pon la operacion, sin espacios u para union, n para interseccion, - para resta, y parentesis, y ! para contrario")
op = input()


