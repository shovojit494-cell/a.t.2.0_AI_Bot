# Animation_Tach AI Bot

A production-oriented Telegram bot for the Animation_Tach brand.

## Included

- Python + python-telegram-bot
- Gemini API for chat, SEO, captions, social writing and coding tools
- Gemini image generation where the configured Gemini model supports it
- Local QR generation, calculator, ZIP create/extract, image crop/resize
- Optional Replicate integration for image/video/audio generation
- Optional remove.bg integration for background removal
- Inline 2-column category menus
- Per-tool prompt flows and Back/Main Menu navigation
- Processing message with Animation_Tach course promotion
- Environment-variable secrets only
- Logging and centralized error handling
- Polling mode suitable for most VPS/container hosting

## Important

Some AI media capabilities require a third-party provider/model. The project does not fabricate results: if a required provider/model key is missing, the bot returns a configuration error. Because Replicate models have different input schemas, the generic adapter currently sends `prompt`; for models requiring image/audio/video files or different field names, add the model-specific adapter in `services/media.py` before production use.

For Replicate tools, put a valid model identifier in the matching `REPLICATE_*_MODEL` variable. Model availability and pricing are controlled by Replicate and can change over time.

## Setup

1. Copy `.env.example` to `.env`.
2. Create a Telegram bot with BotFather and put its token in `BOT_TOKEN`.
3. Create a Gemini API key and put it in `GEMINI_API_KEY`.
4. Install dependencies: `pip install -r requirements.txt`.
5. Run: `python app.py`.

## Hosting

Polling is the default. It works well on VPS, Docker-style hosts, Render/Railway/Fly.io-style long-running workers, and similar services.

The process should be configured as a worker/service running `python app.py`. Restart policy should be enabled by the hosting platform.

Webhook deployment can be added later if your platform specifically requires it; no webhook secret or public URL is hard-coded here.

## Environment variables

### Required
- `BOT_TOKEN`
- `GEMINI_API_KEY`

### Optional
- `GEMINI_MODEL`
- `GEMINI_IMAGE_MODEL`
- `REPLICATE_API_TOKEN`
- `REPLICATE_IMAGE_MODEL`
- `REPLICATE_VIDEO_MODEL`
- `REPLICATE_AUDIO_MODEL`
- `REMOVE_BG_API_KEY`
- `REMOVE_BG_API_URL`
- `APP_BASE_URL`
- `LOG_LEVEL`
- `MAX_DOWNLOAD_MB`

## Brand links

Owner: Reza
Brand: Animation_Tach
WhatsApp: 01995887020
Telegram: @animation_tach
Main Channel: https://t.me/rezaeditzonebd4
Mods Channel: https://t.me/mod_animation_tach
Group: https://t.me/animationtachgroup
TikTok: @animation_tach2.0
TikTok link: https://vm.tiktok.com/ZS9D2wNVNQMX2-l6b1r/

## Course data

2D Short Recorded — 150 BDT — 7 classes
2D Long Recorded — 300 BDT — 15 days / 15 recorded classes
2D Short Live — 299 BDT
2D Long Live — 450 BDT
3D Short Recorded — 250 BDT — 7 days
3D Long Recorded — 400 BDT — 17 recorded classes
3D Short Live — 350 BDT
3D Long Live — 499 BDT

All courses are paid. No free course. No refund after payment. Course materials cannot be shared, resold or reuploaded.

## Media provider notes

`services/replicate.py` contains the real HTTP integration. You choose the model identifier in `.env`; the bot sends the user's input to that provider and waits for the prediction result.

For production, review the provider's current model input/output schema before selecting a model, because different models accept different fields.

## Security

Never commit `.env` or API keys. `.gitignore` excludes `.env`.
