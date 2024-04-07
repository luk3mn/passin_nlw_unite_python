from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError

class CheckInRespository:
    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try: 
                check_in = (
                    CheckIns(attendeeId=attendee_id)
                )
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            except IntegrityError:
                raise Exception("Check In has already registred!")
            except Exception as exception:
                database.session.rollback()
                raise exception