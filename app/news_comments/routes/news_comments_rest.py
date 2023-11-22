from fastapi import APIRouter, Depends

NewsCommentRouter = APIRouter(
    prefix="/news_comments",
    tags=["News Comments"],
)


@NewsCommentRouter.get("/")
def get_ads():
    return "pass"


@NewsCommentRouter.post("/")
def add_ads():
    return "pass"


@NewsCommentRouter.put("/{id}")
def update_ads():
    return "pass"


@NewsCommentRouter.delete("/{id}")
def delete_ads():
    return "pass"
