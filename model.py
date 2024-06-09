from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Guest(BaseModel):
    id: Optional[int] = None  # 기본값을 None으로 설정하여 클라이언트가 제공할 필요 없음을 나타냄
    name: str
    message: str
    timestamp: datetime = datetime.now()
