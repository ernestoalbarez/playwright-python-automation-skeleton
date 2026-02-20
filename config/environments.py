from enum import Enum


class Environment(str, Enum):
    LOCAL = "local"
    STAGING = "staging"
    PROD = "prod"


BASE_URLS: dict[Environment, str] = {
    Environment.LOCAL: "http://localhost:3000",
    Environment.STAGING: "https://staging.example.com",
    Environment.PROD: "https://example.com",
}
