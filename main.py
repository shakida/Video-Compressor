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
         query = ''
         for i in message.command[1:]:
              query += '' + str(i)
         input_url = query
         input_extension="mkv"
         tempid = uuid.uuid4()
         output_path = tempid
         p = await s.send_message(message.chat.id, f'Trying to compress.')
         try:
             proc = await asyncio.create_subprocess_shell(
             f"wget --quiet -O video.{input_extension} {input_url} && mkdir {output_path} && ffmpeg -hide_banner -y -i video.{input_extension} && -vf scale=w=640:h=360:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod  -b:v 800k -maxrate 856k -bufsize 1200k -b:a 96k -hls_segment_filename {output_path}/360p_%03d.ts {output_path}/360p.m3u8 && rm video.{input_extension} && cd {output_path} && echo '# BY SHAKIDA #EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=640x360 360p.m3u8' > master.m3u8",
             asyncio.subprocess.PIPE,
             stderr=asyncio.subprocess.PIPE,
             )
             await p.edit(f'Compressing........')
             await proc.communicate()
             await p.edit(f'✅ Done:\nFile Path: `{output_path}`')
         except Exception as a:
             await p.edit(f'ERROR 69: `{a}`')
      except Exception as a:
         await s.send_message(message.chat.id, f'ERROR X: `{a}`')
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
