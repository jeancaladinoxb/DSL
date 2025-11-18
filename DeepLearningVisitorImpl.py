class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class DeepLearningVisitorImpl:
    def __init__(self):
        self.env_stack = [{}]
        self.functions = {}
        self.models = {}

    def push_env(self):
        self.env_stack.append({})

    def pop_env(self):
        self.env_stack.pop()

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
        def s(v): return 1.0 / (1.0 + (2.718281828459045 ** (-v)))
        if isinstance(x, list):
            return [s(v) for v in x]
        return s(x)

    def _builtin_relu(self, x):
        def r(v): return v if v > 0 else 0
        if isinstance(x, list):
            return [r(v) for v in x]
        return r(x)

    def _builtin_tanh(self, x):
        def t(v):
            e_pos = 2.718281828459045 ** v
            e_neg = 2.718281828459045 ** (-v)
            denom = (e_pos + e_neg)
            return (e_pos - e_neg) / denom if denom != 0 else 0
        if isinstance(x, list):
            return [t(v) for v in x]
        return t(x)

    def _builtin_mse(self, y_true, y_pred):
        n = len(y_true)
        return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n

    def _builtin_mae(self, y_true, y_pred):
        n = len(y_true)
        return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / n

    def _builtin_transpose(self, mat):
        if not mat:
            return []
        rows = len(mat)
        cols = len(mat[0])
        return [[mat[r][c] for r in range(rows)] for c in range(cols)]

    def _builtin_dot(self, a, b):
        if isinstance(a, list) and a and not isinstance(a[0], list) and isinstance(b, list) and b and isinstance(b[0], list):
            cols = len(b[0])
            res = []
            for j in range(cols):
                s = 0
                for i in range(len(a)):
                    s += a[i] * b[i][j]
                res.append(s)
            return res
        if isinstance(a, list) and a and isinstance(a[0], list) and isinstance(b, list) and b and not isinstance(b[0], list):
            res = []
            for row in a:
                s = sum(rv * bv for rv, bv in zip(row, b))
                res.append(s)
            return res
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
        raise NotImplementedError("determinant: solo 2x2 implementado")

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

    def visitProgram(self, ctx):
        for st in ctx.statement():
            self.visit(st)
        return None

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.set_var(name, value)
        return None

    def visitAssignNoSemi(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.set_var(name, value)
        return None

    def visitMatrixDecl(self, ctx):
        name = ctx.ID().getText()
        val = self.visit(ctx.matrixLiteral())
        self.set_var(name, val)
        return None

    def visitMatrixLiteral(self, ctx):
        return [self.visit(r) for r in ctx.row()]

    def visitRow(self, ctx):
        return [self.visit(e) for e in ctx.expr()]

    def visitModelDecl(self, ctx):
        name = ctx.ID().getText()
        if ctx.mlpDecl():
            mlp = self.visit(ctx.mlpDecl())
            self.models[name] = mlp
            self.set_var(name, {"type": "MLP", "spec": mlp})
        else:
            self.models[name] = None
            self.set_var(name, None)
        return None

    def visitMlpDecl(self, ctx):
        in_n = int(self.visit(ctx.expr(0)))
        hid = int(self.visit(ctx.expr(1)))
        out = int(self.visit(ctx.expr(2)))
        return {"input": in_n, "hidden": hid, "output": out}

    def visitPrintStmt(self, ctx):
        args = []
        if ctx.args():
            args = [self.visit(e) for e in ctx.args().expr()]
        self._builtin_print(*args)
        return None

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if cond:
            return self.visit(ctx.block(0))
        elif ctx.ELSE():
            return self.visit(ctx.block(1))
        return None

    def visitBlock(self, ctx):
        self.push_env()
        try:
            for st in ctx.statement():
                self.visit(st)
        except ReturnValue as r:
            self.pop_env()
            raise r
        self.pop_env()
        return None

    def visitForStmt(self, ctx):
        if ctx.getChild(1).getText() == "(":
            self.push_env()
            try:
                self.visit(ctx.assignNoSemi(0))
                while self._is_true(self.visit(ctx.expr())):
                    try:
                        self.visit(ctx.block())
                    except ReturnValue as r:
                        raise r
                    self.visit(ctx.assignNoSemi(1))
            finally:
                self.pop_env()
            return None
        else:
            varname = ctx.ID().getText()
            iterable = self.visit(ctx.expr())
            for v in iterable:
                self.push_env()
                self.define_var(varname, v)
                try:
                    self.visit(ctx.block())
                except ReturnValue as r:
                    self.pop_env()
                    raise r
                self.pop_env()
            return None

    def visitWhileStmt(self, ctx):
        cond_ctx = ctx.expr(0)
        while self._is_true(self.visit(cond_ctx)):
            self.visit(ctx.block())
        return None

    def visitDoWhileStmt(self, ctx):
        while True:
            self.visit(ctx.block())
            if not self._is_true(self.visit(ctx.expr())):
                break
        return None

    def visitFuncDecl(self, ctx):
        name = ctx.ID().getText()
        params = []
        if ctx.params():
            params = [p.getText() for p in ctx.params().ID()]
        block = ctx.block()
        self.functions[name] = (params, block)
        return None

    def visitReturnStmt(self, ctx):
        val = self.visit(ctx.expr())
        raise ReturnValue(val)

    def visitFuncCallExpr(self, ctx):
        if ctx.ID() and ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '(':
            name = ctx.ID().getText()
            args = []
            if ctx.args():
                args = [self.visit(e) for e in ctx.args().expr()]
            if name in self.functions:
                return self._call_user_function(name, self.functions[name][0], self.functions[name][1], args)
            return self._call_builtin(name, args)
        first = ctx.getChild(0).getText()
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '(':
            name = first
            args = []
            if ctx.args():
                args = [self.visit(e) for e in ctx.args().expr()]
            return self._call_builtin(name, args)
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

    def visitExpr(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitEqualityExpr(self, ctx):
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

    def visitRelationalExpr(self, ctx):
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

    def visitAddExpr(self, ctx):
        vals = [self.visit(m) for m in ctx.mulExpr()]
        if len(vals) == 1:
            return vals[0]
        res = vals[0]
        op_idx = 1
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = vals[op_idx]
            if op == "+":
                res = self._binary_add(res, right)
            elif op == "-":
                res = self._binary_sub(res, right)
            op_idx += 1
        return res

    def visitMulExpr(self, ctx):
        vals = [self.visit(p) for p in ctx.powExpr()]
        if len(vals) == 1:
            return vals[0]
        res = vals[0]
        op_idx = 1
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = vals[op_idx]
            if op == "*":
                res = self._binary_mul(res, right)
            elif op == "/":
                res = self._binary_div(res, right)
            elif op == "%":
                res = res % right
            op_idx += 1
        return res

    def visitPowExpr(self, ctx):
        vals = [self.visit(u) for u in ctx.unaryExpr()]
        if len(vals) == 1:
            return vals[0]
        res = vals[0]
        for v in vals[1:]:
            res = res ** v
        return res

    def visitUnaryExpr(self, ctx):
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "-":
            return - self.visit(ctx.unaryExpr())
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx):
        if ctx.NUMBER():
            txt = ctx.NUMBER().getText()
            if '.' in txt:
                return float(txt)
            return int(txt)
        if ctx.STRING():
            s = ctx.STRING().getText()
            return s[1:-1].encode('utf-8').decode('unicode_escape')
        if ctx.ID():
            name = ctx.ID().getText()
            base = self.get_var(name)
            i = 1
            while i < ctx.getChildCount():
                ch = ctx.getChild(i)
                if ch.getText() == '[':
                    expr_ctx = ctx.getChild(i+1)
                    index_val = self.visit(expr_ctx)
                    try:
                        idx = int(index_val)
                    except Exception:
                        idx = index_val
                    base = base[idx]
                    i += 3
                    continue
                i += 1
            return base
        if ctx.matrixLiteral():
            return self.visit(ctx.matrixLiteral())
        if ctx.arrayLiteral():
            return [self.visit(e) for e in ctx.arrayLiteral().expr()]
        if ctx.funcCallExpr():
            return self.visit(ctx.funcCallExpr())
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr())
        raise NotImplementedError("primary no manejado: %s" % ctx.getText())

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
        return result

    def __getattr__(self, name):
        if name.startswith("visit"):
            return lambda ctx: self.visitChildren(ctx)
        raise AttributeError(name)

    def visit(self, node):
        if hasattr(node, "accept"):
            return node.accept(self)
        return None
