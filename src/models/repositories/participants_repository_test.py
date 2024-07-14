import pytest
import uuid

from src.models.settings.db_connection_handler import db_connection_handler

from src.models.repositories.participants_repository import ParticipantsRepository

db_connection_handler.connect()
# participant_id = str(uuid.uuid4())
participant_id = '226f44be-1a51-4485-8e11-54aa249c7c1d'

trip_id = 'd47bc2f9-b17f-4fab-8e97-d0233c1c346f'
emails_to_invite_id = '9646473d-ea8b-4d56-85f8-918e49fccb02'

@pytest.mark.skip(reason="interação com o banco de dados")
def test_create_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "Vinnie"
    }
    
    result = participants_repository.create(participant_infos)
    
    assert result == participant_id
    
@pytest.mark.skip(reason="interação com o banco de dados")
def test_find_trip_participants():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    result = participants_repository.find_participants_from_trip(trip_id)
    
    assert type(result) == list
    
@pytest.mark.skip(reason="interação com o banco de dados")
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    result = participants_repository.update_participant_status(participant_id)
    
    assert result == 1