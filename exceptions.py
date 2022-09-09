class AiportNotFound(Exception):
    def __init__(self, airport_id: int):
        self.message = f"Not found aiport with id {airport_id}"


class TenantNotFound(Exception):
    def __init__(self, subdomain: str):
        self.message = f"Not found tenant with subdomain {subdomain}"
