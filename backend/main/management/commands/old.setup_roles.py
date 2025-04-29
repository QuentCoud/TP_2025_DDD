from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from main.models import User, Artist, ConcertOwner, Admin

class Command(BaseCommand):
    help = 'Création des groupes et permissions de base'


    artist_permissions = ['get_countries']
    owner_permissions = ['get_artists']
    admin_permissions = ['add_user', 'delete_user', 'edit_other', 'add_country', 'edit_country', 'delete_country']

    permissions_rule = {
        'Artist': {
            'rules': artist_permissions,
            'model': Artist
        },
        'ConcertOwner': {
            'rules': owner_permissions,
            'model': ConcertOwner
        },
        'User': {
            'rules': [],
            'model': User 
        },
        'Admin': {
            'rules': list(set(artist_permissions + owner_permissions)),
            'model': Admin 
        }
    }

    def handle(self, *args, **options):
        for group_name, config in self.permissions_rule.items():
            group, created = Group.objects.get_or_create(name=group_name)
            model = config['model']
            content_type = ContentType.objects.get_for_model(model)

            for rule_codename in config['rules']:
                permission, perm_created = Permission.objects.get_or_create(
                    codename=rule_codename,
                    content_type=content_type,
                    defaults={'name': f'Can {rule_codename.replace("_", " ")}'}
                )
                group.permissions.add(permission)

            self.stdout.write(self.style.SUCCESS(f"Groupe '{group_name}' configuré avec ses permissions."))

        self.stdout.write(self.style.SUCCESS('✅ Tous les groupes et permissions ont été créés avec succès.'))