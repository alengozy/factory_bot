# Factory_bot

Django + DRF + Python Telegram API project made for "Фабрика Проектов"

## Usage
1. Open the project via [link](https://octopus-app-c2c2f.ondigitalocean.app/api/docs).
2. Register with the /register endpoint.
3. Obtain the token pair via the "/login" endpoint. Copy the access token.
4. Press the Authorize button in the top right corner, or a lock button next to each endpoint. Paste the token into the field and press Authorize.
5. Open Telegram, find @alengozy_bot, and start the conversation. 
6. Generate your bot token via the "/get_bot_token" endpoint. Copy the resulting token.
7. Send it to the bot, if the bot replies with a success message, you are ready to send messages.
8. Send messages to the bot via the post "/message" endpoint

Note: if you encounter problems with linking the bot token, send a "/reset" command to the bot.
