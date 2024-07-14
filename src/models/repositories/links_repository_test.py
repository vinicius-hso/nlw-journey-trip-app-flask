import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
# trip_id = str(uuid.uuid4())
trip_id = "30ec2a57-68f1-4a7b-9f14-ba8a5b2a06a2"

@pytest.mark.skip(reason="interação com o banco de dados")
def test_create_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    link_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "https://google.com",
        "title": "Google"
    }
    
    links_repository.create_link(link_infos)

# @pytest.mark.skip(reason="interação com o banco de dados")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links = links_repository.find_links_from_trip(trip_id)
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)
    print("\n\n", links, "\n\n")
    