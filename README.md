pysillywalks
============
This is an example project for learning about git and python.

**It is very silly**

Installation
------------
To install, use the standard `python setup.py install`

Quick Usage
-----------
The constructor expects the following keyword arguments:

    - **walk**: A string of the walk type or genre
    - **silly**: An integer rating of the silliness level

Example initialization:

```python
    from pysillywalks import Silly

    s = Silly(walk="pirate", silly=2)
    if s.is_very_silly:
        s.action()
    else:
        print "Not silly enough, sorry!"
```

License
-------
Copyright (c) 2012 Mark Allen

You may use this software under the terms of the [MIT License][]. See the 
LICENSE file for details.

[MIT License]: http://opensource.org/licenses/mit-license.php
