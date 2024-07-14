from src.models.repositories.links_repository import LinksRepository
import uuid

class LinkCreator:
    def __init__(self, links_repository: LinksRepository):
        self.__links_repository = links_repository
        
    def create(self, body, trip_id) -> dict:
        try:
            link_id = str(uuid.uuid4())
            link_infos = {
                "link": body['url'],
                "title": body['title'],
                "id": link_id,
                "trip_id": trip_id
            }
            self.__links_repository.create_link(link_infos)
            return { "body": { "linkId": link_id }, "status_code": 201}
        except Exception as e:
            return {
                "body": { "error": "Bad Request", "message": str(e) },
                "status_code": 400
            }