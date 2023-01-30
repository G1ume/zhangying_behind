class Chapter:
    def __init__(self, chapter_id, chapter_name, chapter_top, chapter_user):
        self.id = chapter_id
        self.name = chapter_name
        self.top = chapter_top
        self.user = chapter_user
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return self

    def toJson(self):
        result = "value:\"{}\",label:\"{}\",children:".format(self.id, self.name)
        children_str = "["
        for child in self.children:
            children_str = children_str + child.toJson() + ","
        if children_str.endswith(","):
            children_str = children_str[:-1]
        children_str += "]"
        return "{" + result + children_str + "}"


if __name__ == '__main__':
    instance = Chapter(0, "new chapter", 0, 0)
    instance.add_child(Chapter(1, "children", 0, 0)).add_child(Chapter(2, "children", 0, 0))
    print(instance.toJson())
