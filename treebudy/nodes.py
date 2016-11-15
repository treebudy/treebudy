# -*- coding: utf-8 -*-
from collections.abc import MutableSequence, MutableMapping
from collections import OrderedDict


class Snode(MutableSequence):
    """An elementtree-like Node/Element object that knows it's parent"""

    # this will allow easy subclassing to extend the container types that can
    # be parsed
    STYPES = (list, tuple)
    MTYPES = (dict, OrderedDict)

    def __init__(self, nodes=None, parent=None):
        self.__children = list()
        self._parent = None
        self.parent = parent

        if nodes:
            self.extend(nodes)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if parent is None:
            self._parent = None
        elif isinstance(parent, (Snode, Mnode)):
            self._parent = parent
        else:
            raise TypeError("Type({}) cannot be a parent of \
                             Type({})".format(type(parent), type(self)))

    def __getitem__(self, index):
        return self.__children[index]

    def __setitem__(self, index, node):

        if isinstance(node, (Snode, Mnode)):
            node.parent = self
            self.__children[index] = node
        elif isinstance(node, self.STYPES):
            self.__children[index] = Snode(node, parent=self)
        else:
            self.__children[index] = node

    def __delitem__(self, index):
        del self.__children[index]

    def __len__(self):
        return len(self.__children)

    def insert(self, index, node):
        """insert something as a child of this node. If that something derives
        from MutableSequence it will be converted into an Snode

        """

        if isinstance(node, (Snode, Mnode)):
            node.parent = self
            self.__children.insert(index, node)
        elif isinstance(node, self.STYPES):
            self.__children.insert(index, Snode(node, parent=self))
        else:
            self.__children.insert(index, node)


class Mnode(MutableMapping):
    """A mapping elementtree-like Node/Element object that knows it's parent

    Parameters
    ----------
    parent: Mnode or Snode

    """
    STYPES = (list, tuple)
    MTYPES = (dict, OrderedDict)
    def __init__(self, nodes=None, parent=None):
        self.__children = OrderedDict()
        self._parent = None
        if nodes:
            self.__children.update(nodes)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if parent is None:
            self._parent = None
        elif isinstance(parent, (Snode, Mnode)):
            self._parent = parent
        else:
            raise TypeError("Type({}) cannot be a parent of \
                             Type({})".format(type(parent), type(self)))

    def __iter__(self):
        for node_name in self.__children:
            yield node_name

    def __getitem__(self, key):
        return self.__children[key]

    def __setitem__(self, key, node):
        self.__children[key] = node

    def __delitem__(self, key):
        del self.__children[key]

    def __len__(self):
        return len(self.__children)
