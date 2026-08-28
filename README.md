# [Official bot](https://t.me/MessageLoggingBot) 

## Telegram private message logging based on Telegram Business features

This bot was designed for those who would like to receive some kind of notification when someone edits or 
deletes messages in a personal dialogue with them.

To ensure the security of message storage, an encryption system is used based on the `connection_id` parameter 
which Telegram transmits when connecting a bot to a profile and which is unique for each user, which 
allows you to guarantee complete safety of messages.

### List of supported message types:
- Text message
- Media message with caption (Photo/Video/GIF/Voice/Audio)
- Media message without caption (Photo/Video/GIF/Voice/Audio)
- Stickers
- Video note
- Location (It is not saved in the database, so when changed, only the current coordinates are displayed)

### Known Issues:
- **Rich Messages and other new message types are currently unsupported!** Due to the different structure of such messages it will require
huge change to the database structure or increase of storage usage. I will think how to better store this type of message,
but support of them will be delayed.

- Messages you received before connecting to the bot cannot be tracked.
- Unfortunately, due to the fact that the `connection_id` is unique for each connection - when disconnecting the bot from the profile
all your messages will be deleted from the database because they will never be able to be decrypted in the future, which means further 
storage makes no sense.

### List of supported UI languages:
- English
- Ukrainian
- Russian