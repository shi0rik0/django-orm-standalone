import init as _

from site_package.models import Person
import sys

Person(name=sys.argv[1], age=int(sys.argv[2])).save()
