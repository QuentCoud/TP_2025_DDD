from django.core.management.base import BaseCommand
from main.models import Country
import csv
import os
from django.conf import settings
from main.constants import COUNTRY_CODE

class Command(BaseCommand):
  help = 'Remplit la base de données avec les pays à partir d\'un fichier CSV.'
  
  def handle(self, *args, **options):
    file_path = os.path.join(settings.BASE_DIR, 'data', 'data.csv')

    if not os.path.exists(file_path):
        self.stdout.write(self.style.ERROR(f"❌ Le fichier {file_path} n'existe pas."))
        return

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            country_code = row.get('country')
            if not country_code:
                self.stdout.write(self.style.WARNING(f"⛔ Ligne ignorée : Pas de code trouvé : {row}"))
                continue

            country_name = COUNTRY_CODE.get(country_code)

            if not country_name:
                self.stdout.write(self.style.WARNING(f"⚠️ Code pays inconnu '{country_code}', ligne ignorée."))
                continue
            
            field_mapping = {
              'name': country_name,
              "slug": row.get("country"),  
              "rap_hip_hop": float(row.get("Rap/Hip Hop")),
              "pop": float(row.get("Pop")),
              "electro": float(row.get("Electro")),
              "rnb": float(row.get("R&B")),
              "films_jeux_video": float(row.get("Films/Jeux vidéo")),
              "rock_hard_rock": float(row.get("Rock/Hard Rock")),
              "techno_house": float(row.get("Techno/House")),
              "country_music": float(row.get("Country")),
              "trance": float(row.get("Trance")),
              "reggae": float(row.get("Reggae")),
              "population_total": float(row.get("population_total")),
              "life_expectancy": float(row.get("life_expectancy")),
              "birth_rate": float(row.get("birth_rate")),
              "avg_income": float(row.get("avg_income"))
            } 
            
            # Créer ou mettre à jour le pays
            country, created = Country.objects.update_or_create(
                slug=country_code,
                defaults=field_mapping
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Pays créé : {country_name} ({country_code})"))
            else:
                self.stdout.write(self.style.SUCCESS(f"🔄 Pays mis à jour : {country_name} ({country_code})"))

        self.stdout.write(self.style.SUCCESS('🎉 Remplissage terminé !'))