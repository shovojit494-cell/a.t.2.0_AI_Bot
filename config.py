import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    bot_token: str = os.getenv("BOT_TOKEN", "")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    gemini_image_model: str = os.getenv("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")
    replicate_api_token: str = os.getenv("REPLICATE_API_TOKEN", "")
    replicate_image_model: str = os.getenv("REPLICATE_IMAGE_MODEL", "")
    replicate_video_model: str = os.getenv("REPLICATE_VIDEO_MODEL", "")
    replicate_audio_model: str = os.getenv("REPLICATE_AUDIO_MODEL", "")
    remove_bg_api_key: str = os.getenv("REMOVE_BG_API_KEY", "")
    remove_bg_api_url: str = os.getenv("REMOVE_BG_API_URL", "https://api.remove.bg/v1.0/removebg")
    app_base_url: str = os.getenv("APP_BASE_URL", "")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    max_download_mb: int = int(os.getenv("MAX_DOWNLOAD_MB", "50"))

settings = Settings()

if not settings.bot_token:
    raise RuntimeError("BOT_TOKEN is required.")
