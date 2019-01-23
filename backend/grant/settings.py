# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SITE_URL = env.str('SITE_URL', default='https://grant.io')
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
QUEUES = ["default"]
SECRET_KEY = env.str("SECRET_KEY")
BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False

SENDGRID_API_KEY = env.str("SENDGRID_API_KEY", default="")
SENDGRID_DEFAULT_FROM = "noreply@grant.io"

SENTRY_DSN = env.str("SENTRY_DSN", default=None)
SENTRY_RELEASE = env.str("SENTRY_RELEASE", default=None)

MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB (limits file uploads, raises RequestEntityTooLarge)

AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = env.str("AWS_DEFAULT_REGION")
S3_BUCKET = env.str("S3_BUCKET")

SECURITY_USER_IDENTITY_ATTRIBUTES = ['email_address']  # default is 'email'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = SECRET_KEY

GITHUB_CLIENT_ID = env.str("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = env.str("GITHUB_CLIENT_SECRET")
TWITTER_CLIENT_ID = env.str("TWITTER_CLIENT_ID")
TWITTER_CLIENT_SECRET = env.str("TWITTER_CLIENT_SECRET")
LINKEDIN_CLIENT_ID = env.str("LINKEDIN_CLIENT_ID")
LINKEDIN_CLIENT_SECRET = env.str("LINKEDIN_CLIENT_SECRET")

BLOCKCHAIN_REST_API_URL = env.str("BLOCKCHAIN_REST_API_URL")
BLOCKCHAIN_API_SECRET = env.str("BLOCKCHAIN_API_SECRET")

ADMIN_PASS_HASH = env.str("ADMIN_PASS_HASH")

EXPLORER_URL = env.str("EXPLORER_URL", default="https://explorer.zcha.in/")
