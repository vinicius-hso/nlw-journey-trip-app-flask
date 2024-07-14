from src.models.repositories.links_repository import LinksRepository

class LinkFinder:
    def __init__(self, links_repository: LinksRepository):
        self.__links_repository = links_repository
        
    def find(self, tripId) -> dict:
        try:
            links = self.__links_repository.find_links_from_trip(tripId)
            
            formatted_links = []
            for link in links:
                formatted_links.append({
                    "id": link[0],
                    "url": link[2],
                    "title": link[3]
                })
            return { 
                    "body": { "links": formatted_links }, 
                    "status_code": 200 
            }
        except Exception as e:
            return {
                "body": { "error": "Bad Request", "message": str(e) },
                "status_code": 400
            }