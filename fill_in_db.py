from webapp import create_app
from webapp.model import RealEstateAds
from webapp.parsers.flats import get_flats_snippets

app = create_app()
with app.app_context():
    get_flats_snippets()

