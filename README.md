django_didactics
================

Organize your lessons &amp; attachments

You can create courses for a specific subject and then prepare your own lessons with attachments (pdf, ppt...).
Attachments can be categorized depending on the type (i.e. Homeworks, Tests, Exercises & Solutions....) .

Now its is admin-side only (no front-end).


Dependencies
------------------

Django>= 1.5


Examples
--------

The application is in didactics folder; django_didactics is just a demo project.
Sync your database first, then run the server.
1) python manage.py syncdb

2) python manage.py runserver


LICENSE
---------------

Copyright 2014 Luca Sturaro

Released under the MIT License. See LICENSE.txt.


ToDo
--------

Provide a ListView for Front end showing in a table all Courses and Lessons with attachments