from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from main.models import User, Artist, ConcertOwner, Admin

class Command(BaseCommand):
    help = 'Création des groupes et permissions de base'

    permissions_rule = {
        'Artist': {'rules': ['get_country'], 'model': ContentType.objects.get_for_model(Artist) },
        'ConcertOwner': {'rules': ['get_artists'], 'model': ContentType.objects.get_for_model(ConcertOwner) },
        'User': {'rules': ['edit_me'], 'model': ContentType.objects.get_for_model(User) },
        'Admin': {'rules': ['add_user', 'edit_user', 'delete_user'], 'model': ContentType.objects.get_for_model(Admin) }
    }

    def handle(self, *args, **options):
        # Créer les groupes
        artiste_group, _ = Group.objects.get_or_create(name='artist')
        proprio_group, _ = Group.objects.get_or_create(name='concertOwner')
        admin_group, _ = Group.objects.get_or_create(name='admin')

        self.stdout.write(self.style.SUCCESS('Groupes créés ou existants'))

        # Exemple : ajouter des permissions
        # Tu peux adapter ça à tes modèles
        # Ici juste un exemple pour les permissions de base User

        user_content_type = ContentType.objects.get_for_model(User)

        print(self.permissions_rule)

        for e in self.permissions_rule:
            print(e)
            
        # for rule in list(self.permissions_rule.keys()):
        #     for permission in self.permissions_rule[rule]:
        #         try:
        #             permission_obj = Permission.objects.get(codename=permission, content_type=user_content_type)
        #             if rule == 'Artist':
        #                 artiste_group.permissions.add(permission_obj)
        #             elif rule == 'ConcertOwner':
        #                 proprio_group.permissions.add(permission_obj)
        #             elif rule == 'Admin':
        #                 admin_group.permissions.add(permission_obj)
        #         except Permission.DoesNotExist:
        #             self.stdout.write(self.style.WARNING(f'Permission {permission} non trouvée pour le modèle {rule}'))
        # can_change = Permission.objects.get(codename='change_user', content_type=user_content_type)

        # artiste_group.permissions.add(can_change)
        # self.stdout.write(self.style.SUCCESS('Permissions ajoutées au groupe Artiste'))