# Beta version
# By me (tg-@shakida69)
import os
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.raw import functions, types
import pyrogram
from os import path
import uuid
import subprocess
import asyncio
import wget


shakida = Client(
    ":memory:",
    '2177518',
    '6f700167aeed1f5d546eab443e85bd7d',
    bot_token='1851824879:AAHu_kSVPmJusQOVGE9y_f7RLcMoym_jgwg')
shakida.start()
shakida.send_message(-1001297289773, f'🍑 Alive')



@shakida.on_message(filters.command(["compo"]) & filters.group & ~ filters.edited)
async def live(s: shakida, message: Message):
       try:
          tempid = uuid.uuid4()
          videos = message.reply_to_message
          if videos.video or videos.document:
             f = await s.send_message(message.chat.id, f'📥 **Downloading..**')
          try:
             video = await s.download_media(videos)
         #   os.system(f'ffmpeg -i "{video}" -vn -f s16le -ac 2 -ar 48000 -acodec pcm_s16le VID-{}.raw -y')
        #    audio = f'VID-{message.chat.id}.raw'
          except Exception as e:
             await f.edit(f'**ERROR!:**\n`{e}`')
             return
          try:
             await f.edit(f'**🗜️ Compressing...**')
             proc = await asyncio.create_subprocess_shell(
             f'ffmpeg -hide_banner -loglevel quiet -i "{video}" -preset ultrafast -vcodec libx265 -crf 27 "VID-{tempid}.mkv" -y',
             stdout=asyncio.subprocess.PIPE,
             stderr=asyncio.subprocess.PIPE,
             )
             await proc.communicate()
             out = f"VID-{tempid}.mkv"
             await f.edit(f'**COMPRESSION SUCCESSFULLY DONE ✅**\n`File Uploading...`')
             await s.send_video(message.chat.id, out, caption=f'✅ UPLOADED SUCCESSFULLY.\nEngine: `FFMAPG` Preset: `Ultrafast` CRF: `27` Quality: `Standard`')
             os.remove(f'VID-{tempid}.mkv')
             os.remove(video)
             await f.delete()
          except Exception as a:
             await s.send_message(message.chat.id, f'**ERROR!:**\n`{a}`')
       except Exception as a:
          await s.send_message(message.chat.id, f'**ERROR!!**\n`{a}`')
          return



@shakida.on_message(filters.command("ss") & filters.group)
async def shell(client: shakida, message: Message):
    cmd = message.text.split(' ', 1)
    if len(cmd) == 1:
        await message.reply_text('**No command to execute was given!**')
        return
    cmd = cmd[1]
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    reply = ''
    stderr = stderr.decode()
    stdout = stdout.decode()
    if stdout:
        reply += f"⚙️**Stdout**\n`{stdout}`\n"
    if stderr:
        reply += f"⚙️**Stderr**\n`{stderr}`\n"
    if len(reply) > 3000:
        with open('shell_output.txt', 'w') as file:
            file.write(reply)
        with open('shell_output.txt', 'rb') as doc:
            client.send_document(
                document=doc,
                filename=doc.name,
                reply_to_message_id=message.message_id,
                chat_id=message.chat_id)
    else:
        await message.reply_text(reply)


idle()
