from fastapi import APIRouter, HTTPException, Path
from model import Guest
from typing import List
from datetime import datetime

guest_router = APIRouter()

guest_list: List[Guest] = []
guest_counter = 0


# 방명록 추가
@guest_router.post("/guest")
async def add_guest(guest: Guest) -> dict:
    global guest_counter
    guest.id = guest_counter = guest_counter + 1
    guest.timestamp = datetime.now()  # 타임스탬프 설정
    guest_list.append(guest)
    return {
        "msg": "Guest added successfully",
        "guest": guest
    }

@guest_router.get("/guest")
async def retrieve_guest() -> dict:
    # 방명록 목록을 타임스탬프 기준으로 내림차순 정렬
    sorted_guest_list = sorted(guest_list, key=lambda x: x.timestamp, reverse=True)
    return {
        "guest": sorted_guest_list
    }
    
    
# 경로 파라미터 추가
@guest_router.get("/guest/{guest_id}") 
async def get_single_guest(guest_id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
    for guest in guest_list:
        if guest.id == guest_id:
            return guest
    raise HTTPException(status_code=404, detail="Guest with supplied ID doesn't exist")

# 방명록 삭제 
@guest_router.delete("/guest/{guest_id}")
async def delete_guest(guest_id: int) -> dict:
    global guest_list
    for guest in guest_list:
        if guest.id == guest_id:
            guest_list.remove(guest)
            return {
                "msg": "Guest deleted successfully"
            }
    raise HTTPException(status_code=404, detail="Guest with supplied ID doesn't exist")