# -*- coding: utf-8 -*-
from collections.abc import MutableSequence, MutableMapping
from collections import OrderedDict


class Snode(MutableSequence):
    """An elementtree-like Node/Element object that knows it's parent"""
    def __init__(self, parent, nodes=None):
        self.__children = list()
        self._parent = None
        if nodes:
            self.__children.extend(nodes)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if isinstance(parent, (Snode, Mnode)):
            self._parent = parent

    def __getitem__(self, index):
        return self.__children[index]

    def __setitem__(self, index, node):
        self.__children[index] = node

    def __delitem__(self, index):
        del self.__children[index]

    def __len__(self):
        return len(self.__children)

    def insert(self, index, node):
        self.__children[index] = node


class Mnode(MutableMapping):
    """A mapping elementtree-like Node/Element object that knows it's parent

    Parameters
    ----------
    parent: Mnode or Snode

    """

    def __init__(self, parent, nodes=None):
        self.__children = OrderedDict()
        self._parent = None
        if nodes:
            self.__children.update(nodes)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if isinstance(parent, (Snode, Mnode)):
            self._parent = parent

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
