from contextlib import asynccontextmanager

import uvicorn
from app import exceptions, handlers
from app.ads.routes.ads_rest import AdsRouter
from app.brand_admins.routes.brand_admin_rest import AdminRouter
from app.brand_subscribers.routes.subscribers_rest import SubscriberRouter
from app.brands.routes.brands_rest import BrandRouter
from app.config import get_settings, set_logger
from app.credential.routes.credentials_rest import CredentialRouter
from app.database import db
from app.emailer.routes.emailer_rest import MailerRouter
from app.live_news.routes.live_news_rest import LiveNewsRouter
from app.live_news_comments.routes.live_news_comments_rest import LiveCommentRouter
from app.news.routes.news_rest import NewsRouter
from app.news_comments.routes.news_comments_rest import NewsCommentRouter
from app.subscriptions.routes.subscriptions_rest import SubscriptionRouter
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

DB_SESSION = None
DB_AUTH = None
settings = get_settings()
settings.db_session = db.get_session()
set_logger()


@asynccontextmanager
async def lifespan(f_app: FastAPI):
    global DB_SESSION
    DB_SESSION = db.get_session()
    global DB_AUTH
    DB_AUTH = DB_SESSION.auth()
    # user = DB_AUTH.sign_in_with_email_and_password(email=settings.db_user, password=settings.db_user_pass)
    yield


app = FastAPI(
    lifespan=lifespan,
    debug=True if settings.environment == "local" else False,
    title="NPaaS",
    description='Now you can own your own news channels and livestreams',
    version="1.0.0",
    dependencies=[],
)

# app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.add_exception_handler(exceptions.NPaaSException, handlers.npaas_exception_handler)
app.add_exception_handler(exceptions.CredentialsExistException, handlers.credential_exception_handler)
app.add_exception_handler(exceptions.CredentialsNotFoundException, handlers.no_credential_exception_handler)
app.add_exception_handler(exceptions.LoginRequiredException, handlers.login_needed_handler)

app.include_router(AdsRouter)
app.include_router(AdminRouter)
app.include_router(SubscriptionRouter)
app.include_router(SubscriberRouter)
app.include_router(BrandRouter)
app.include_router(CredentialRouter)
app.include_router(MailerRouter)
app.include_router(LiveNewsRouter)
app.include_router(LiveCommentRouter)
app.include_router(NewsRouter)
app.include_router(NewsCommentRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info", reload=True, port=9000)
