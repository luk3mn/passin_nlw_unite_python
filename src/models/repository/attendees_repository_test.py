from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New database insert")
def test_insert_attendee():
    event_id = "meu-uuid-e-nois"
    attentees_info = {
        "uuid": "meu_uuid_attendee",
        "name": "attendee name",
        "email": "email@email.com",
        "event_id": event_id
    }
    attentees_repository = AttendeesRepository()
    response = attentees_repository.insert_attendeee(attentees_info)
    print(response)

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendee_id = "meu_uuid_attendee"
    attendee_repository = AttendeesRepository()
    attende = attendee_repository.get_attendee_badge_by_id(attendee_id)

    print(attende)
    print(attende.title)
