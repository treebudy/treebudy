===============================
treebudy
===============================


.. image:: https://img.shields.io/pypi/v/treebudy.svg
        :target: https://pypi.python.org/pypi/treebudy

.. image:: https://img.shields.io/travis/drafter250/treebudy.svg
        :target: https://travis-ci.org/drafter250/treebudy

.. image:: https://readthedocs.org/projects/treebudy/badge/?version=latest
        :target: https://treebudy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/drafter250/treebudy/shield.svg
     :target: https://pyup.io/repos/github/drafter250/treebudy/
     :alt: Updates


What
----

Treebudy Aims to offer two variations of The basic list(Sequence) and Dict(Mapping) types in
Python. The Snode and the Mnode. The main difference from a normal List or dict
is that they keep a reference to their parent container.

Why
---

My main Frustration with a number of libraries having to do with data serialization
formats like xml, json & yaml is that I always run into the problem that once
I have searched through them to find the piece of data I need I sometimes need
to also know where it is in the nested hierarchy of containers. The only object
type I know of in the Standard Library that does this is the Node object in the
xml mini-dom library. However the xml.etree.ElementTree API is much nicer to
work with. The one thing it lacks is that parental reference. When it comes to
Json and Yaml they simply get turned into lists and Dicts so no luck there.

Of note the wildley popular third party library lxml provides an interface
virtually identical to the elementree api as well as provide a method to get the
previous parent element. However lxml is a C based library and the goal here is
lightweight and zero dependencies and also it's for xml not Json or yaml.

My main use case for creating this library is that i want to be able to
index a file directory tree in json or yaml, look for a particular file
and then create a path to the file by tracing back up through the tree.

You would normaly have to come up with some fancy algorithm to do this. but being
able to ask an element who it's parent is much simpler.

Project Status
--------------

Just barely started - this is my first try at creating an open source project.


* Free software: BSD license
* Documentation: https://drafter250.github.io/treebudy/


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
