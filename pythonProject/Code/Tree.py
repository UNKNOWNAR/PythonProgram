class Tree:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level +=1
        return level

    def print_tree(self):
        spaces = " "*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = Tree("Electronics")
    laptop = Tree("Laptop")
    gaming_laptop = Tree("Gaming Laptop")
    business_laptop = Tree("Business Laptop")

    laptop.add_child(gaming_laptop)
    laptop.add_child(business_laptop)

    phone = Tree("Phone")
    smartphone = Tree("Smartphone")
    feature_phone = Tree("Feature Phone")

    phone.add_child(smartphone)
    phone.add_child(feature_phone)

    tv = Tree("Television")
    led_tv = Tree("LED TV")
    oled_tv = Tree("OLED TV")

    tv.add_child(led_tv)
    tv.add_child(oled_tv)

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    return root

if __name__=="__main__":
    root = build_tree()
    root.print_tree()