=====
Usage
=====

To use treebudy in a project::

    from treebudy import nodes

    root = nodes.Snode([1,2,3])
    child1 = nodes.Snode([4,5,6])
    root.append(child1)
    child1.parent is root
