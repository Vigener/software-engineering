# ファイル treetest.py
from tree import Tree

root = Tree("A",
  Tree("B",
    Tree("C", None, None),
    Tree("D", None, None)),
  Tree("E",
    Tree("F", None, None),
    None))

for node in root:
  print(node._label)
