# coding: utf-8
import sys
from django.core.management.base import NoArgsCommand
import random
from django.db import transaction

from tuitter.models import Tuit
from profiles.models import get_max_id, get_random_user

TUITS_TO_CREATE = 10000

class Command(NoArgsCommand):
    help = "Create test users"

    def print_progress(self, cnt, total):
        if not cnt % 100:
            print "%.2f%% done" % (cnt*100./total)

    def handle_noargs(self, **options):
        try:
            max_user_id = get_max_id()

            with transaction.commit_on_success():
                for i in xrange(TUITS_TO_CREATE):
                    self.print_progress(i, TUITS_TO_CREATE)
                    t = Tuit(status="Some status " + str(random.randint(0, 1024)), user=get_random_user(max_user_id))
                    t.save()

        except Exception:
            import traceback
            traceback.print_exc(file=sys.stdout)
