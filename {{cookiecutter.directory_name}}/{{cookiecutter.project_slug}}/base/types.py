from datetime import datetime

import strawberry


@strawberry.interface
class BaseType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
