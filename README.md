# 747Disco - Marketing & Vendite Eventi Assistant

Assistente AI per marketing e vendite di eventi privati - 747Disco Ciampino (Roma)

![screen_shot](./image/screen_shot_1.gif)

## git clone

```
git clone https://github.com/festiva1300/streamlit-claude-chat.git
cd streamlit-claude-chat
```

## environment setting

Write the Anthripic access key, the model to be used in the `.env` file.

```
API_KEY=XX-XXXXX...
AI_MODEL=claude-3-sonnet-20240229
```

## execute

### build a container

```bash
docker build ./ -t streamlit-claude-chat
```

### deploy on local

```bash
docker compose up -d
```

