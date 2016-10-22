# -*- coding: utf-8 -*-
from collections.abc import MutableSequence, MutableMapping
from collections import OrderedDict


class Snode(MutableSequence):
    """An elementtree-like Node/Element object that knows it's parent"""
    def __init__(self, nodes=None):
        self.__children = list()
        if nodes:
            self.__children.extend(nodes)

    def __getitem__(self, index):
        return self.__children[index]

    def __setitem__(self, index, node):
        if isinstance(node, (Snode, Mnode)):
            self.__children[index] = node
        else:
            raise TypeError

    def __delitem__(self, index):
        del self.__children[index]

    def __len__(self):
        return len(self.__children)

    def insert(self, index, node):
        if isinstance(node, (Snode, Mnode)):
            self.__children[index] = node
        else:
            raise TypeError


class Mnode(MutableMapping):
    """A mapping elementtree-like Node/Element object that knows it's parent"""

    def __init__(self, nodes=None):
        self.__children = OrderedDict()
        if nodes:
            self.__children.update(nodes)

    def __iter__(self):
        for node_name in self.__children:
            yield node_name

    def __getitem__(self, key):
        return self.__children[key]

    def __setitem__(self, key, node):
        if isinstance(node, (Snode, Mnode)):
            self.__children[key] = node
        else:
            raise TypeError

    def __delitem__(self, key):
        del self.__children[key]

    def __len__(self):
        return len(self.__children)
