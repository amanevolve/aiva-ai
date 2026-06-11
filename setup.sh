#!/bin/bash

echo "🚀 Starting Aiva AI Setup..."

# 1. Build and start the Docker containers in detached mode (-d)
echo "📦 Building and starting containers..."
docker compose up -d --build

# 2. Give the Ollama container a few seconds to fully boot up
echo "⏳ Waiting for the Ollama engine to boot (10 seconds)..."
sleep 10

# 3. Download the AI model directly inside the running container
echo "🧠 Downloading the tinyllama AI model (~637MB). This might take a moment..."
docker exec aiva-ollama ollama pull tinyllama

echo "✅ Setup Complete! Aiva AI is now running."
echo "🌐 Open your web browser and navigate to http://<YOUR-EC2-PUBLIC-IP> to start chatting!"o

