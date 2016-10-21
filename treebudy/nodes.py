# -*- coding: utf-8 -*-
from collections.abc import MutableSequence, MutableMapping
from collections import OrderedDict


class Snode(MutableSequence):
    """An elementtree-like Node/Element object that knows it's parent"""
    def __init__(self, nodes=None):
        self.__sequence = list()
        if nodes:
            self.__sequence.extend(nodes)

    def __getitem__(self, index):
        return self.__sequence[index]

    def __setitem__(self, index, node):
        if isinstance(node, (Snode, Mnode)):
            self.__sequence[index] = node
        else:
            raise TypeError

    def __delitem__(self, index):
        del self.__sequence[index]

    def __len__(self):
        return len(self.__sequence)

    def insert(self, index, node):
        if isinstance(node, (Snode, Mnode)):
            self.__sequence[index] = node
        else:
            raise TypeError


class Mnode(MutableMapping):
    """A mapping elementtree-like Node/Element object that knows it's parent"""
    def __init__(self, nodes=None):
        self.__children = OrderedDict()
        if nodes:
            self.__children.update(nodes)
    def __iter__(self):
        for node_name in self.__children.

    def __getitem__(self, key):
        return self.__sequence[key]

    def __setitem__(self, key, node):
        if isinstance(node, (Snode, Mnode)):
            self.__children[key] = node
        else:
            raise TypeError

    def __delitem__(self, key):
        del self.__children[key]

    def __len__(self):
        return len(self.children)
