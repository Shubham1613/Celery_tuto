from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def add(x,y):
    return x+y
add.apply_async((3,3), countdown=5)
