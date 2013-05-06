# coding: utf-8
import sys
from django.core.management.base import NoArgsCommand
import factory
import random
from tuitter.models import Tuit
from profiles.models import get_max_id, get_random_user


class Command(NoArgsCommand):
    help = "Create test users"

    def print_progress(self, cnt, total):
        if not cnt % 100:
            print "%.2f%% done" % (cnt*100./total)

    def handle_noargs(self, **options):
        try:
            max_user_id = get_max_id()

            class TuitFactory(factory.Factory):
                FACTORY_FOR = Tuit
                status = "Some status " + str(random.randint(0, 1024))
                user = get_random_user(max_user_id)

            for i in xrange(10000):
                self.print_progress(i, 10000)
                TuitFactory.create()

        except Exception:
            import traceback
            traceback.print_exc(file=sys.stdout)
