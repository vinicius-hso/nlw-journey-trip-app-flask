from sqlite3 import Connection

class ParticipantsRepository:
    def __init__(self, conn: Connection):
        self.__conn = conn
    
    def create(self, participant_infos: dict) -> str:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO participants
                    (id, trip_id, emails_to_invite_id, name)
                VALUES
                    (?, ?, ?, ?)
                RETURNING id
            ''', (
                participant_infos['id'],
                participant_infos['trip_id'],
                participant_infos['emails_to_invite_id'],
                participant_infos['name'],
            )
        )
        data = cursor.fetchone()[0]
        self.__conn.commit()
        
        return data
    
    def find_participants_from_trip(self, trip_id):
        cursor =  self.__conn.cursor()
        cursor.execute(
            '''
                SELECT p.id, p.name, p.is_confirmed, e.email 
                FROM participants AS p
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            ''', (trip_id,)
        )
        data = cursor.fetchall()
        return data
    
    # TODO: atualzar status do participante
    def update_participant_status(self, participant_id) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE participants
                SET is_confirmed = 1
                WHERE id = ?
                RETURNING is_confirmed
            ''', (participant_id,)
        )
        result = cursor.fetchone()[0]
        self.__conn.commit()
        
        return result