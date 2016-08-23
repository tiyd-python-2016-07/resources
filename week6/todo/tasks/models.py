from django.db import models
import datetime


def get_repr(o):
    args = [
        "{}={}".format(key, repr(value))
        for key, value in o.__dict__.items()
        if not key.startswith('_')
    ]
    return "{}({})".format(o.__class__.__name__, ', '.join(args))

models.Model.__repr__ = models.Model.__str__ = get_repr


class Task(models.Model):
    BACKLOG = 1
    READY = 2
    DOING = 3
    BLOCKED = 4
    DONE = 5

    STATUSES = {
        BACKLOG: 'Backlog',
        READY: 'Ready',
        DOING: 'Doing',
        BLOCKED: 'Blocked',
        DONE: 'Done',
    }

    description = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUSES.items(), default=BACKLOG)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_status(self):
        return self.STATUSES[self.status]

    def __str__(self):
        return "Task(id={id}, description=\"{description}\", status={status}, created=\"{created}\", updated=\"{updated}\")".format(**self.__dict__)
