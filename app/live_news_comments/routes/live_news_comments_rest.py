from fastapi import APIRouter, Depends

LiveCommentRouter = APIRouter(
    prefix="/live_news_comments",
    tags=["Live News Comments"],
)


@LiveCommentRouter.get("/")
def get_ads():
    return "pass"


@LiveCommentRouter.post("/")
def add_ads():
    return "pass"


@LiveCommentRouter.put("/{id}")
def update_ads():
    return "pass"


@LiveCommentRouter.delete("/{id}")
def delete_ads():
    return "pass"
