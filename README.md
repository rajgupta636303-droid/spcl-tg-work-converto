# Telegram Converter Bot

A powerful Telegram bot that converts PDFs to images, images to PDFs, and changes image formats.

## Features

- 📄 PDF to Images (with page selection)
- 🖼️ Images to PDF
- 🎨 Image Format Conversion
- ⚡ Live progress tracking
- 📊 Smart page selection (all/range/specific)

## Deployment on Render

### Step 1: Push to GitHub
1. Create a new repository on GitHub
2. Push all files to the repository

### Step 2: Deploy on Render
1. Go to [Render.com](https://render.com)
2. Click **New** → **Web Service**
3. Connect your GitHub repository
4. Render will auto-detect the `render.yaml` configuration

### Step 3: Add Environment Variable
1. In Render Dashboard, go to your service
2. Click **Environment**
3. Add: `BOT_TOKEN` = your_telegram_bot_token

### Step 4: Deploy
Click **Create Web Service** and wait for deployment to complete.

## Local Development

