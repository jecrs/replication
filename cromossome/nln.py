class Element:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.childs = []
        self.parent = None
        self.parlist = []
        self.hyearchy_lvl = -1

def parse(content):
    lmnts = {}
    plmnts:list[Element] = []

    def parseplmnt(line):
        if ":" in line:
            name, value = line.split(":", 1)
            return Element(name.strip(), value.strip())
        return None

    for l in content.splitlines():
        l = l.strip()
        if not l:
            continue

        hl = 0
        while hl < len(l) and l[hl] == "-":
            hl += 1

        clean_line = l[hl:].strip() if hl > 0 else l.strip()
        lmnt = parseplmnt(clean_line)

        if lmnt is None:
            continue

        lmnt.hyearchy_lvl = hl

        if hl > 0:
            for o in reversed(plmnts):
                if o.hyearchy_lvl == hl - 1:
                    lmnt.parent = plmnts.index(o)
                    o.childs.append(len(plmnts))
                    break

        plmnts.append(lmnt)

    for l in plmnts:
        if l.parent is not None:
            par = []
            current = plmnts[l.parent]
            while current:
                par.append(current.name)
                if current.parent is not None:
                    current = plmnts[current.parent]
                else:
                    break
            l.parlist = list(reversed(par))

    for l in plmnts:
        if l is None:
            continue
        loc = lmnts
        for k in l.parlist:
            loc = loc.setdefault(k, {})
        
        if l.childs == []:
            loc[l.name] = l.value
            continue
        loc[l.name] = {"_val": l.value}

    return lmnts
