from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_token: str = "changeme"
    oscp_mode: bool = True
    db_url: str = "sqlite:///data/redops.db"
    redis_url: str = "redis://localhost:6379/0"
    max_concurrency: int = 4
    wordlist_dir: str = "data/wordlists"
    profiles_dir: str = "data/profiles"
    snapshots_dir: str = "data/snapshots"
    denylist_imds: bool = True
    pdf_branding: str = "RedOps"

    class Config:
        env_prefix = "REDOPS_"

settings = Settings()
