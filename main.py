from fastapi import FastAPI
from guest import guest_router  # guest_router 불러오기
from fastapi.middleware.cors import CORSMiddleware  #CORS 미들웨어
import uvicorn

app = FastAPI()

# 개발환경에서 테스트하는 프론트 주소,  nginx와 연결되어있는 public ip 주소
origins = ["http://127.0.0.1:5500", "http://34.202.129.139/"]

# 미들웨어 추가 
app.add_middleware(
	CORSMiddleware,
	allow_origins= origins,
	allow_credentials = True,
	allow_methods = ["*"],
	allow_headers= ["*"],
)



@app.get("/")
async def welcome() -> dict:
	return {
	   	"msg" : "hello world?"
	}
	

app.include_router(guest_router)

if __name__ == '__main__':
		uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)