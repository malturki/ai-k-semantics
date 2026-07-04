result = True

def identity(cls):
    return cls

class Plain:
    seed = 4

    def __init__(self, start=seed, /, *items, scale, offset=1, **kw):
        self.total = start * scale + len(items) + offset + kw["bonus"] + len(kw)

    def var_only(self, value, /, *items):
        return self.total + value + len(items)

    def var_default(self, value=seed, /, *items):
        return self.total + value + len(items)

    def kw_only(self, value, /, **kw):
        return self.total + value + kw["bonus"] + len(kw)

    def kw_default(self, value=seed, /, **kw):
        return self.total + value + kw["bonus"] + len(kw)

    def both(self, value, /, *items, **kw):
        return self.total + value + len(items) + kw["bonus"] + len(kw)

    def both_default(self, value=seed, /, *items, **kw):
        return self.total + value + len(items) + kw["bonus"] + len(kw)

    def mixed_required(self, value, /, *items, flag):
        return self.total + value + len(items) + flag

    def mixed(self, value=seed, /, *items, flag=2, offset=1):
        return self.total + value + len(items) + flag + offset

    def full(self, value, /, *items, flag, **kw):
        return self.total + value + len(items) + flag + kw["bonus"] + len(kw)

    def full_default(self, value=seed, /, *items, flag=2, offset=1, **kw):
        return self.total + value + len(items) + flag + offset + kw["bonus"] + len(kw)

    def no_var_full(self, value, /, *, flag, **kw):
        return self.total + value + flag + kw["bonus"] + len(kw)

    def no_var_full_default(self, value=seed, /, *, flag=2, offset=1, **kw):
        return self.total + value + flag + offset + kw["bonus"] + len(kw)

    seed = 40

class Child(Plain):
    pass

p = Plain(2, 5, 6, scale=3, offset=4, bonus=7, tag=9)
q = Plain(scale=2, bonus=3)
child = Child(scale=1, bonus=2)

plain_ok = (
    p.total == 21
    and q.total == 13
    and child.total == 8
    and p.var_only(1, 2, 3) == 24
    and Plain.var_only(p, 2, 3) == 24
    and q.var_default() == 17
    and p.kw_only(1, bonus=2, extra=3) == 26
    and q.kw_default(bonus=5) == 23
    and p.both(1, 2, 3, bonus=4) == 29
    and q.both_default(7, 8, bonus=1, extra=2) == 24
    and p.mixed_required(1, 2, 3, flag=4) == 28
    and q.mixed(flag=3) == 21
    and p.full(1, 2, flag=3, bonus=4, extra=5) == 32
    and q.full_default(flag=3, bonus=4) == 26
    and p.no_var_full(1, flag=2, bonus=3, extra=4) == 29
    and q.no_var_full_default(bonus=5) == 26
    and child.full_default(flag=2, bonus=3) == 19
)

class StaticTools:
    seed = 5

    @staticmethod
    def svar(value, /, *items):
        return value + len(items)

    @staticmethod
    def svard(value=seed, /, *items):
        return value + len(items)

    @staticmethod
    def skw(value, /, **kw):
        return value + kw["bonus"] + len(kw)

    @staticmethod
    def skwd(value=seed, /, **kw):
        return value + kw["bonus"] + len(kw)

    @staticmethod
    def sboth(value, /, *items, **kw):
        return value + len(items) + kw["bonus"] + len(kw)

    @staticmethod
    def sbothd(value=seed, /, *items, **kw):
        return value + len(items) + kw["bonus"] + len(kw)

    @staticmethod
    def smix(value, /, *items, flag):
        return value + len(items) + flag

    @staticmethod
    def smixd(value=seed, /, *items, flag=2, offset=1):
        return value + len(items) + flag + offset

    @staticmethod
    def sfull(value, /, *items, flag, **kw):
        return value + len(items) + flag + kw["bonus"] + len(kw)

    @staticmethod
    def sfulld(value=seed, /, *items, flag=2, offset=1, **kw):
        return value + len(items) + flag + offset + kw["bonus"] + len(kw)

    @staticmethod
    def snovar(value, /, *, flag, **kw):
        return value + flag + kw["bonus"] + len(kw)

    @staticmethod
    def snovard(value=seed, /, *, flag=2, offset=1, **kw):
        return value + flag + offset + kw["bonus"] + len(kw)

    seed = 50

staticmethod_ok = (
    StaticTools.svar(1, 2, 3) == 3
    and StaticTools.svard() == 5
    and StaticTools.skw(1, bonus=2, extra=3) == 5
    and StaticTools.skwd(bonus=4) == 10
    and StaticTools.sboth(1, 2, 3, bonus=4) == 8
    and StaticTools.sbothd(7, 8, bonus=1, extra=2) == 11
    and StaticTools.smix(1, 2, 3, flag=4) == 7
    and StaticTools.smixd(flag=3) == 9
    and StaticTools.sfull(1, 2, flag=3, bonus=4, extra=5) == 11
    and StaticTools.sfulld(flag=3, bonus=4) == 14
    and StaticTools.snovar(1, flag=2, bonus=3, extra=4) == 8
    and StaticTools.snovard(bonus=5) == 14
)

class ClassTools:
    seed = 6
    kind = 10

    @classmethod
    def cvar(cls, value, /, *items):
        return cls.kind + value + len(items)

    @classmethod
    def cvard(cls, value=seed, /, *items):
        return cls.kind + value + len(items)

    @classmethod
    def ckw(cls, value, /, **kw):
        return cls.kind + value + kw["bonus"] + len(kw)

    @classmethod
    def ckwd(cls, value=seed, /, **kw):
        return cls.kind + value + kw["bonus"] + len(kw)

    @classmethod
    def cboth(cls, value, /, *items, **kw):
        return cls.kind + value + len(items) + kw["bonus"] + len(kw)

    @classmethod
    def cbothd(cls, value=seed, /, *items, **kw):
        return cls.kind + value + len(items) + kw["bonus"] + len(kw)

    @classmethod
    def cmix(cls, value, /, *items, flag):
        return cls.kind + value + len(items) + flag

    @classmethod
    def cmixd(cls, value=seed, /, *items, flag=2, offset=1):
        return cls.kind + value + len(items) + flag + offset

    @classmethod
    def cfull(cls, value, /, *items, flag, **kw):
        return cls.kind + value + len(items) + flag + kw["bonus"] + len(kw)

    @classmethod
    def cfulld(cls, value=seed, /, *items, flag=2, offset=1, **kw):
        return cls.kind + value + len(items) + flag + offset + kw["bonus"] + len(kw)

    @classmethod
    def cnovar(cls, value, /, *, flag, **kw):
        return cls.kind + value + flag + kw["bonus"] + len(kw)

    @classmethod
    def cnovard(cls, value=seed, /, *, flag=2, offset=1, **kw):
        return cls.kind + value + flag + offset + kw["bonus"] + len(kw)

    seed = 60

class MoreClassTools(ClassTools):
    kind = 100

classmethod_ok = (
    ClassTools.cvar(1, 2, 3) == 13
    and ClassTools.cvard() == 16
    and ClassTools.ckw(1, bonus=2, extra=3) == 15
    and ClassTools.ckwd(bonus=4) == 21
    and ClassTools.cboth(1, 2, 3, bonus=4) == 18
    and ClassTools.cbothd(7, 8, bonus=1, extra=2) == 21
    and ClassTools.cmix(1, 2, 3, flag=4) == 17
    and ClassTools.cmixd(flag=3) == 20
    and ClassTools.cfull(1, 2, flag=3, bonus=4, extra=5) == 21
    and ClassTools.cfulld(flag=3, bonus=4) == 25
    and ClassTools.cnovar(1, flag=2, bonus=3, extra=4) == 18
    and ClassTools.cnovard(bonus=5) == 25
    and MoreClassTools.cfulld(flag=2, bonus=3) == 113
    and getattr(MoreClassTools(), "cnovard")(bonus=4) == 114
)

@identity
class Decorated:
    seed = 3

    def calc(self, value=seed, /, *items, flag=2, **kw):
        return value + len(items) + flag + kw["bonus"] + len(kw)

@identity
class DecoratedChild(Decorated):
    def add(self, value, /, *, flag, **kw):
        return self.calc(value, flag=flag, bonus=kw["bonus"]) + len(kw)

decorated_ok = (
    Decorated().calc(bonus=4) == 10
    and Decorated().calc(2, 5, 6, flag=3, bonus=4, extra=1) == 13
    and DecoratedChild().add(4, flag=5, bonus=6, extra=7) == 18
)

missing_pos = False
try:
    p.kw_only(value=1, bonus=2)
except TypeError:
    missing_pos = True

missing_kwonly = False
try:
    p.mixed_required(1)
except TypeError:
    missing_kwonly = True

staticmethod_missing_pos = False
try:
    StaticTools.skw(value=1, bonus=2)
except TypeError:
    staticmethod_missing_pos = True

classmethod_missing_kwonly = False
try:
    ClassTools.cmix(1)
except TypeError:
    classmethod_missing_kwonly = True

errors_ok = missing_pos and missing_kwonly and staticmethod_missing_pos and classmethod_missing_kwonly

result = plain_ok and staticmethod_ok and classmethod_ok and decorated_ok and errors_ok
assert result
result
