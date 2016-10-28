#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_treebudy
----------------------------------

Tests for `treebudy` module.
"""

import pytest


from treebudy.nodes import Snode, Mnode


# @pytest.fixture
# def response():
#     """Sample pytest fixture.
#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     import requests
#     return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_SNode_init():
    """Simple Instantiation test for sequence Node type."""
    root = Snode()
    assert isinstance(root, Snode)


def test_MNode_init():
    """Simple Instantiation test for mapping Node type."""
    root = Mnode()
    assert isinstance(root, Mnode)


def test_Snode_init_with_flat_list():
    slist = Snode([1, 2, 3, 4])
    assert 1 in slist
    assert 2 in slist
    assert 3 in slist
    assert 4 in slist


def test_Snode_one_level_deep():
    slist0 = Snode([1, 2, 3, 4])
    slist1 = Snode([1, 2, 3])
    slist0.append(slist1)
    assert slist1 in slist0
    assert slist1.parent is slist0
    print(slist1)
