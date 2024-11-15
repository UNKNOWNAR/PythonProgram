class ManagementTree:
    def __init__(self,data,designation):
        self.name = data
        self.designation = designation
        self.parent = None
        self.children = []

    def add_child(self,child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def print(self,instruction,level=4):
        if level==0:
            return
        spaces = " " * self.get_level() * 3
        line = spaces+"|__"
        if instruction == "name":
            line += self.name
        elif instruction == "designation":
            line += self.designation
        elif instruction == "both":
            line += self.name+"("+self.designation+")"
        print (line)
        if len(self.children) > 0:
            for element in self.children:
                element.print(instruction,level-1)

def build_tree():
    ceo = ManagementTree("Nilpul","CEO")
    cto = ManagementTree("Chinmay","CTO")
    ceo.add_child(cto)
    ih = ManagementTree("Vishwa","Infrastructure Head")
    cto.add_child(ih)
    ah = ManagementTree("Aamir","Application Head")
    cto.add_child(ah)
    cm = ManagementTree("Dhaval","Cloud Manager")
    am = ManagementTree("Abhijit","Application Manager")
    ih.add_child(cm)
    ih.add_child(am)
    hh = ManagementTree("Gels","HR Head")
    rm = ManagementTree("Peter","Recruitment Manager")
    pm = ManagementTree("Waqas","Policy Manager")
    ceo.add_child(hh)
    hh.add_child(rm)
    hh.add_child(pm)
    return ceo

if __name__=="__main__":
    root = build_tree()
    root.print("both",3)