import random

import mimesis

class ApiPlaceholderBody:
    def create_resource_body(self, resource_id: int = None):
        body = {
            "title": mimesis.Person('ru').first_name(),
            "body": mimesis.Person('ru').telephone(),
            "userId": random.randint(100, 200)
        }
        if resource_id:
            body['id'] = resource_id
        return body
