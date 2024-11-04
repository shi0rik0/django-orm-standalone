import init as _

from site_package.models import Person

print(Person.objects.all().values())
