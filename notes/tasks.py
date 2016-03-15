from __future__ import absolute_import

from notesapp import celery
from celery import shared_task, task

import time

#@shared_task
@task
def test(param):
    time.sleep(10)
    return 'this test task executed with argument %s" ' % param
