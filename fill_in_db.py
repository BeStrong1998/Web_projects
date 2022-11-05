from webapp import create_app
from webapp.parsers.flats import get_flats_snippets, get_flat_content

app = create_app()
with app.app_context():
    get_flats_snippets()
    get_flat_content()