# Visitor implementado para DeepLearning (ANTLR4)
# Requiere DeepLearningVisitor.py y DeepLearningParser.py generados por ANTLR
from DeepLearningVisitor import DeepLearningVisitor
from DeepLearningParser import DeepLearningParser

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value


class DeepLearningVisitorImpl(DeepLearningVisitor):
    def __init__(self):
        super().__init__()
        self.env_stack = [{}]
        self.functions = {}
        self.models = {}

# Entornos / variables
    def push_env(self):
        self.env_stack.append({})

    def pop_env(self):
        if len(self.env_stack) > 1:
            self.env_stack.pop()
        else:
            self.env_stack[-1] = {}

    def define_var(self, name, value):
        self.env_stack[-1][name] = value

    def set_var(self, name, value):
        for env in reversed(self.env_stack):
            if name in env:
                env[name] = value
                return
        self.env_stack[-1][name] = value

    def get_var(self, name):
        for env in reversed(self.env_stack):
            if name in env:
                return env[name]
        raise NameError("Variable '%s' no definida" % name)

# Builtins
    def _builtin_print(self, *args):
        print(*args)

    def _builtin_len(self, x):
        return len(x)

    def _builtin_range(self, a, b=None):
        if b is None:
            return list(range(int(a)))
        return list(range(int(a), int(b)))

    def _builtin_sum(self, arr):
        return sum(arr)

    def _builtin_mean(self, arr):
        if not arr:
            return 0
        return sum(arr) / len(arr)

    def _builtin_std(self, arr):
        if not arr:
            return 0
        mean = self._builtin_mean(arr)
        var = sum((x - mean) ** 2 for x in arr) / len(arr)
        return var ** 0.5

    def _builtin_sigmoid(self, x):
        import math
        def s(v): return 1.0 / (1.0 + math.exp(-v))
        if isinstance(x, list):
            return [s(v) for v in x]
        return s(x)

    def _builtin_relu(self, x):
        def r(v): return v if v > 0 else 0
        if isinstance(x, list):
            return [r(v) for v in x]
        return r(x)

    def _builtin_tanh(self, x):
        import math
        def t(v): return math.tanh(v)
        if isinstance(x, list):
            return [t(v) for v in x]
        return t(x)

    def _builtin_mse(self, y_true, y_pred):
        n = len(y_true)
        if n == 0:
            return 0
        return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n

    def _builtin_mae(self, y_true, y_pred):
        n = len(y_true)
        if n == 0:
            return 0
        return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / n

    def _builtin_transpose(self, mat):
        if not mat:
            return []
        rows = len(mat)
        cols = len(mat[0])
        return [[mat[r][c] for r in range(rows)] for c in range(cols)]

    def _builtin_dot(self, a, b):
        # vector x matriz
        if isinstance(a, list) and a and not isinstance(a[0], list) and isinstance(b, list) and b and isinstance(b[0], list):
            cols = len(b[0])
            res = []
            for j in range(cols):
                s = 0
                for i in range(len(a)):
                    s += a[i] * b[i][j]
                res.append(s)
            return res
        # matriz x vector
        if isinstance(a, list) and a and isinstance(a[0], list) and isinstance(b, list) and b and not isinstance(b[0], list):
            res = []
            for row in a:
                s = sum(rv * bv for rv, bv in zip(row, b))
                res.append(s)
            return res
        # matriz x matriz
        if isinstance(a, list) and a and isinstance(a[0], list) and isinstance(b, list) and b and isinstance(b[0], list):
            rows = len(a)
            cols = len(b[0])
            inner = len(b)
            res = [[0] * cols for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    s = 0
                    for k in range(inner):
                        s += a[i][k] * b[k][j]
                    res[i][j] = s
            return res
        raise TypeError("dot: tipos incompatibles")

    def _builtin_determinant(self, mat):
        if len(mat) == 1 and not isinstance(mat[0], list):
            return mat[0]
        if len(mat) == 2 and len(mat[0]) == 2:
            a, b = mat[0]
            c, d = mat[1]
            return a * d - b * c
        raise NotImplementedError("determinant: solo 1xN o 2x2 implementado")

    def _builtin_inverse(self, mat):
        det = self._builtin_determinant(mat)
        if det == 0:
            raise ValueError("inverse: matriz singular")
        a, b = mat[0]
        c, d = mat[1]
        inv = [[d / det, -b / det], [-c / det, a / det]]
        return inv

    def _builtin_normalize(self, arr):
        mn = min(arr)
        mx = max(arr)
        if mx == mn:
            return [0 for _ in arr]
        return [(x - mn) / (mx - mn) for x in arr]

    def _call_builtin(self, name, args):
        nl = name.lower()
        if nl == "print":
            return self._builtin_print(*args)
        if nl == "len":
            return self._builtin_len(args[0])
        if nl == "range":
            return self._builtin_range(*args)
        if nl == "sum":
            return self._builtin_sum(args[0])
        if nl == "mean":
            return self._builtin_mean(args[0])
        if nl == "std":
            return self._builtin_std(args[0])
        if nl == "sigmoid":
            return self._builtin_sigmoid(args[0])
        if nl == "relu":
            return self._builtin_relu(args[0])
        if nl == "tanh":
            return self._builtin_tanh(args[0])
        if nl == "mse":
            return self._builtin_mse(args[0], args[1])
        if nl == "mae":
            return self._builtin_mae(args[0], args[1])
        if nl == "transpose":
            return self._builtin_transpose(args[0])
        if nl == "dot":
            return self._builtin_dot(args[0], args[1])
        if nl == "determinant":
            return self._builtin_determinant(args[0])
        if nl == "inverse":
            return self._builtin_inverse(args[0])
        if nl == "normalize":
            return self._builtin_normalize(args[0])
        if nl == "zeros":
            rows, cols = int(args[0]), int(args[1])
            return [[0 for _ in range(cols)] for _ in range(rows)]
        if nl == "ones":
            rows, cols = int(args[0]), int(args[1])
            return [[1 for _ in range(cols)] for _ in range(rows)]
        if nl == "identity":
            n = int(args[0])
            return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        raise NotImplementedError("Builtin '%s' no implementado" % name)

# Visitors
    def visitProgram(self, ctx: DeepLearningParser.ProgramContext):
        for st in ctx.statement():
            self.visit(st)
        return None

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: DeepLearningParser.AssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.set_var(name, value)
        return None

    def visitAssignNoSemi(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.set_var(name, value)
        return None

    def visitMatrixDecl(self, ctx: DeepLearningParser.MatrixDeclContext):
        name = ctx.ID().getText()
        val = self.visit(ctx.matrixLiteral())
        self.set_var(name, val)
        return None

    def visitMatrixLiteral(self, ctx: DeepLearningParser.MatrixLiteralContext):
        return [self.visit(r) for r in ctx.row()]

    def visitRow(self, ctx: DeepLearningParser.RowContext):
        return [self.visit(e) for e in ctx.expr()]

    def visitModelDecl(self, ctx: DeepLearningParser.ModelDeclContext):
        name = ctx.ID().getText()
        if ctx.mlpDecl():
            mlp = self.visit(ctx.mlpDecl())
            self.models[name] = mlp
            self.set_var(name, {"type": "MLP", "spec": mlp})
        else:
            self.models[name] = None
            self.set_var(name, None)
        return None

    def visitMlpDecl(self, ctx: DeepLearningParser.MlpDeclContext):
        in_n = int(self.visit(ctx.expr(0)))
        hid = int(self.visit(ctx.expr(1)))
        out = int(self.visit(ctx.expr(2)))
        return {"input": in_n, "hidden": hid, "output": out}

    def visitPrintStmt(self, ctx: DeepLearningParser.PrintStmtContext):
        args = []
        if ctx.args():
            args = [self.visit(e) for e in ctx.args().expr()]
        self._builtin_print(*args)
        return None

    def visitIfStmt(self, ctx: DeepLearningParser.IfStmtContext):
        cond = self.visit(ctx.expr())
        if cond:
            return self.visit(ctx.block(0))
        elif ctx.ELSE():
            return self.visit(ctx.block(1))
        return None

    def visitBlock(self, ctx: DeepLearningParser.BlockContext):
        self.push_env()
        try:
            for st in ctx.statement():
                self.visit(st)
        except ReturnValue as r:
            self.pop_env()
            raise r
        self.pop_env()
        return None

    def visitForStmt(self, ctx: DeepLearningParser.ForStmtContext):
        if ctx.IN():
            varname = ctx.ID().getText()
            expr_ctx = ctx.expr()
            iterable = self.visit(expr_ctx)
            if iterable is None:
                raise TypeError(f"El iterable en 'for {varname} in ...' evaluo a None. Expresion: {expr_ctx.getText()}")
            try:
                iterator = iter(iterable)
            except TypeError:
                raise TypeError(f"El valor proporcionado a 'for {varname} in' no es iterable: {iterable!r} (expresion: {expr_ctx.getText()})")
            for v in iterator:
                self.push_env()
                self.define_var(varname, v)
                try:
                    self.visit(ctx.block())
                except ReturnValue as r:
                    self.pop_env()
                    raise r
                self.pop_env()
            return None

        else:
            self.push_env()
            try:
                if ctx.assignNoSemi(0):
                    self.visit(ctx.assignNoSemi(0))
                cond_ctx = ctx.expr()
                while True:
                    cond_ok = True
                    if cond_ctx is not None:
                        cond_val = self.visit(cond_ctx)
                        cond_ok = self._is_true(cond_val)
                    if not cond_ok:
                        break
                    try:
                        self.visit(ctx.block())
                    except ReturnValue as r:
                        raise r
                    if ctx.assignNoSemi(1):
                        self.visit(ctx.assignNoSemi(1))
            finally:
                self.pop_env()
            return None

    def visitWhileStmt(self, ctx: DeepLearningParser.WhileStmtContext):
        cond_ctx = ctx.expr()
        while self._is_true(self.visit(cond_ctx)):
            self.visit(ctx.block())
        return None

    def visitDoWhileStmt(self, ctx: DeepLearningParser.DoWhileStmtContext):
        while True:
            self.visit(ctx.block())
            if not self._is_true(self.visit(ctx.expr())):
                break
        return None

    def visitFuncDecl(self, ctx: DeepLearningParser.FuncDeclContext):
        name = ctx.ID().getText()
        params = []
        if ctx.params():
            params = [p.getText() for p in ctx.params().ID()]
        block = ctx.block()
        self.functions[name] = (params, block)
        return None

    def visitReturnStmt(self, ctx: DeepLearningParser.ReturnStmtContext):
        val = self.visit(ctx.expr())
        raise ReturnValue(val)

    def _call_user_function(self, name, params, block, args):
        self.push_env()
        try:
            for p, a in zip(params, args):
                self.define_var(p, a)
            try:
                self.visit(block)
            except ReturnValue as r:
                return r.value
        finally:
            self.pop_env()
        return None

    def visitFuncCallExpr(self, ctx: DeepLearningParser.FuncCallExprContext):
        """
        Maneja llamadas:
          - FUNCTION_OR_KEYWORD '(' args? ')'
          - ID '.' ID '(' args? ')'  (metodo)
        """
        # Caso: func(...) donde el primer hijo puede ser un ID o una keyword token
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '(':
            name = ctx.getChild(0).getText()
            args = []
            if ctx.args():
                args = [self.visit(e) for e in ctx.args().expr()]
            if name in self.functions:
                params, block = self.functions[name]
                return self._call_user_function(name, params, block, args)
            return self._call_builtin(name, args)

        # Caso metodo: ID DOT ID LPAREN args? RPAREN
        if ctx.getChildCount() >= 4 and ctx.getChild(1).getText() == '.':
            obj_name = ctx.ID(0).getText()
            method = ctx.ID(1).getText()
            obj = self.get_var(obj_name)
            args = []
            if ctx.args():
                args = [self.visit(e) for e in ctx.args().expr()]
            if isinstance(obj, dict) and obj.get("type") == "MLP":
                if method.lower() == "train":
                    obj["last_train"] = {"args": args}
                    return None
                if method.lower() == "predict":
                    return [0] * obj["spec"]["output"]
            raise NotImplementedError("Method call %s.%s no implementado" % (obj_name, method))

        return None

# Expresiones
    def visitExpr(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitEqualityExpr(self, ctx: DeepLearningParser.EqualityExprContext):
        vals = [self.visit(r) for r in ctx.relationalExpr()]
        if len(vals) == 1:
            return vals[0]
        res = vals[0]
        op_idx = 1
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = vals[op_idx]
            if op == "==":
                res = (res == right)
            elif op == "!=":
                res = (res != right)
            op_idx += 1
        return res

    def visitRelationalExpr(self, ctx: DeepLearningParser.RelationalExprContext):
        vals = [self.visit(a) for a in ctx.addExpr()]
        if len(vals) == 1:
            return vals[0]
        res = vals[0]
        op_idx = 1
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = vals[op_idx]
            if op == "<":
                res = res < right
            elif op == "<=":
                res = res <= right
            elif op == ">":
                res = res > right
            elif op == ">=":
                res = res >= right
            op_idx += 1
        return res

    def visitAddExpr(self, ctx: DeepLearningParser.AddExprContext):
        vals = [self.visit(m) for m in ctx.mulExpr()]
        if len(vals) == 1:
            return vals[0]
        
        for i, v in enumerate(vals):
            if v is None:
                raise ValueError(f"El operando {i} en addExpr evaluo a None: {ctx.getText()}")
        
        res = vals[0]
        op_idx = 1
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            if op_idx >= len(vals):
                break
            right = vals[op_idx]
            if op == "+":
                res = self._binary_add(res, right)
            elif op == "-":
                res = self._binary_sub(res, right)
            op_idx += 1
        return res

    def visitMulExpr(self, ctx: DeepLearningParser.MulExprContext):
        vals = [self.visit(p) for p in ctx.powExpr()]
        if len(vals) == 1:
            return vals[0]
            
        for i, v in enumerate(vals):
            if v is None:
                raise ValueError(f"El operando {i} en mulExpr evaluo a None")
        
        res = vals[0]
        op_idx = 1
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            if op_idx >= len(vals):
                break
            right = vals[op_idx]
            if op == "*":
                res = self._binary_mul(res, right)
            elif op == "/":
                res = self._binary_div(res, right)
            elif op == "%":
                res = res % right
            op_idx += 1
        return res

    def visitPowExpr(self, ctx: DeepLearningParser.PowExprContext):
        vals = [self.visit(u) for u in ctx.unaryExpr()]
        
        for i, v in enumerate(vals):
            if v is None:
                raise ValueError(f"El operando {i} en powExpr evaluo a None. Expresion: {ctx.getText()}")
        
        if len(vals) == 1:
            return vals[0]
        
        res = vals[0]
        for v in vals[1:]:
            res = res ** v
        return res

    def visitUnaryExpr(self, ctx: DeepLearningParser.UnaryExprContext):
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "-":
            val = self.visit(ctx.unaryExpr())
            if val is None:
                raise ValueError(f"Operando unario evaluo a None. Expresion: {ctx.getText()}")
            return -val
        result = self.visit(ctx.primary())
        if result is None:
            raise ValueError(f"Primary evaluo a None. Expresion: {ctx.getText()}")
        return result

    def visitPrimary(self, ctx: DeepLearningParser.PrimaryContext):
        # Caso 1: NUMBER
        if ctx.NUMBER():
            txt = ctx.NUMBER().getText()
            if '.' in txt:
                return float(txt)
            return int(txt)
        
        # Caso 2: STRING
        if ctx.STRING():
            s = ctx.STRING().getText()
            return s[1:-1].encode('utf-8').decode('unicode_escape')
        
        # Caso 3: Expresion entre parentesis: ( expr )
        # Verificar primero si empieza con '('
        if ctx.getChildCount() >= 3 and ctx.getChild(0).getText() == "(":
            # El hijo en posicion 1 debe ser la expresion
            expr_node = ctx.getChild(1)
            result = self.visit(expr_node)
            if result is None:
                raise ValueError(f"Expresion en parentesis evaluo a None: {expr_node.getText()}")
            return result
        
        # Caso 4: ID con posible indexacion
        if ctx.ID():
            name = ctx.ID().getText()
            base = self.get_var(name)
            
            # Verificar si hay indexacion usando ctx.expr()
            expr_list = ctx.expr()
            
            if expr_list:
                # expr_list puede ser una lista o un solo elemento
                if not isinstance(expr_list, list):
                    expr_list = [expr_list]
                
                for expr_node in expr_list:
                    index_val = self.visit(expr_node)
                    
                    # Convertir a entero si es posible
                    try:
                        idx = int(index_val)
                    except (ValueError, TypeError):
                        idx = index_val
                    
                    # Aplicar indexacion
                    if base is None:
                        raise ValueError(f"Intento de indexar variable '{name}' que es None")
                    
                    try:
                        base = base[idx]
                    except (IndexError, KeyError, TypeError) as e:
                        raise ValueError(f"Error al indexar '{name}[{idx}]': {e}")
            
            return base
        
        # Caso 5: matrixLiteral
        if ctx.matrixLiteral():
            return self.visit(ctx.matrixLiteral())
        
        # Caso 6: arrayLiteral
        if ctx.arrayLiteral():
            return [self.visit(e) for e in ctx.arrayLiteral().expr()]
        
        # Caso 7: funcCallExpr
        if ctx.funcCallExpr():
            return self.visit(ctx.funcCallExpr())
        
        raise NotImplementedError("primary no manejado: %s" % ctx.getText())

# Operaciones auxiliares
    def _binary_add(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x + y for x, y in zip(a, b)]
        if isinstance(a, list) and not isinstance(b, list):
            return [x + b for x in a]
        if isinstance(b, list) and not isinstance(a, list):
            return [a + x for x in b]
        return a + b

    def _binary_sub(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x - y for x, y in zip(a, b)]
        if isinstance(a, list) and not isinstance(b, list):
            return [x - b for x in a]
        if isinstance(b, list) and not isinstance(a, list):
            return [a - x for x in b]
        return a - b

    def _binary_mul(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x * y for x, y in zip(a, b)]
        if isinstance(a, list) and not isinstance(b, list):
            return [x * b for x in a]
        if isinstance(b, list) and not isinstance(a, list):
            return [a * x for x in b]
        return a * b

    def _binary_div(self, a, b):
        if isinstance(a, list) and isinstance(b, list):
            return [x / y for x, y in zip(a, b)]
        if isinstance(a, list) and not isinstance(b, list):
            return [x / b for x in a]
        if isinstance(b, list) and not isinstance(a, list):
            return [a / x for x in b]
        return a / b

    def _is_true(self, v):
        if isinstance(v, list):
            return len(v) > 0
        return bool(v)

    def visitChildren(self, node):
        result = None
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            if hasattr(child, "accept"):
                result = child.accept(self)
            else:
                result = None
        return result

    def __getattr__(self, name):
        if name.startswith("visit"):
            return lambda ctx: self.visitChildren(ctx)
        raise AttributeError(name)

    def visit(self, node):
        if hasattr(node, "accept"):
            return node.accept(self)
        return None
