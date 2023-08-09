from environs import Env

env = Env()
env.read_env()


SECRET_KEY = env.str("SECRET_KEY")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")

BASE_URL = env.str("BASE_URL")
TOKEN = env.str("TOKEN")


# User API url
CREATE_PRODUCT_API_URL = "api/v1/products/create"
DELETE_PRODUCT_API_URL = "api/v1/products/product/delete"