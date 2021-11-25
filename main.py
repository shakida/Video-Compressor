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
from typing import Union
import asyncio
import wget
from datetime import datetime
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psutil
from psutil._common import bytes2human
self_or_contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)
import wget

shakida = Client(
    ":memory:",
    '2177518',
    '6f700167aeed1f5d546eab443e85bd7d',
    bot_token='1851824879:AAHu_kSVPmJusQOVGE9y_f7RLcMoym_jgwg')
shakida.start()
shakida.send_message(-1001297289773, f'🍑 Alive')
temp = []

        
@shakida.on_message(filters.command(["compo"]) & filters.group & ~ filters.edited)
async def compox(s: shakida, message: Message):
          global temp
          tempid = uuid.uuid4()
          video = message.reply_to_message
          any = message.from_user.id
         # crf = 27
          f = await s.send_message(message.chat.id, f"**🔄 Prosesing**")
   #    try:
          if not video.video or video.document:
             url = video.text
             await f.edit(f'**🔄 Prosesing**\n**🏷️`{url}`')
          if len(message.command) != 2:
             crf = 27
          if len(message.command) == 2:
             crf = int(message.text.split(None)[1])
          if (crf < 20) or (crf > 50):
             await f.edit(f'**ERROR!**\nCRF 20-50 value only or default 27')
             return
          if video.video or video.document:
             file_n = video.video.file_name
             ch = video.video.mime_type.split('/')[1]
             file = f'{video.video.file_unique_id}.{ch}'
             butt = InlineKeyboardMarkup([[
                      InlineKeyboardButton("⚙️ Status", callback_data=f"sys"),
               ]])
             temp.append(str(file))
             await f.edit(f'🏷️ `{file_n}`\n**📥 Downloading..**\n'
             + f'**🍻 CC:** {message.from_user.first_name}', reply_markup=butt)
             try:
                videox = await video.download(file)
             except:
                temp.pop(0)
                return
          if not video.video or video.document:
           try:
             file_n = url
             ff = file_n.split(".")
             x = len(ff)
             xt = x-1
             gg = file_n.split(".")[xt]
             file = f'fuckyoubaby.{gg}'
             putt = f'downloads/{file}'
             butt = InlineKeyboardMarkup([[
                      InlineKeyboardButton("⚙️ Status", callback_data=f"sys"),
               ]])
             
             await f.edit(f'🏷️ `{file_n}`\n**📥 Downloading..**\n'
             + f'**🍻 CC:** {message.from_user.first_name}', reply_markup=butt)
             save_dir = 'downloads'
             cmd = r'c:\aria2\aria2c.exe -d '+ save_dir +' -m 5 -o ' + file + " "+ file_n
         #    cmd = f'wget -O {putt} {file_n}'
             lol = await asyncio.create_subprocess_shell(
             f'{cmd}',
             stdout=asyncio.subprocess.PIPE,
             stderr=asyncio.subprocess.PIPE,
             )
             videox = putt
             temp.append(str(file))
             await lol.communicate()
           except Exception as e:
             temp.pop(0)
             await f.edit(f'**ERROR‼️**: LINK ERROR ❌\nUse direct link or end with .mp4, .mkv, .raw, .avi, etc\n`{e}`')
             return
          try:
             but = InlineKeyboardMarkup([[
                InlineKeyboardButton("❌ Cancel", callback_data=f'cl {file}|{crf}|{any}'),
                InlineKeyboardButton("⚙️ Status", callback_data=f"sys"),
                ]])
             await f.edit(f'🏷️` {file_n}`\n**🗜️ Compressing...**\n**⚙️ CRF Range:** `{crf}`\n'
             + f'**🍻 CC:** {message.from_user.first_name}', reply_markup=but)
             proc = await asyncio.create_subprocess_shell(
             f'ffmpeg -hide_banner -loglevel quiet -i "{videox}" -preset ultrafast -vcodec libx265 -crf {crf} "{file}" -y',
             stdout=asyncio.subprocess.PIPE,
             stderr=asyncio.subprocess.PIPE,
             )
             await proc.communicate()
             out = f"{file}"
             os.remove(videox)
             await f.edit(f'`🏷️ {file_n}`\n**COMPRESSION SUCCESSFULLY DONE ✅**\n**📤 File Uploading...**\n'
             + f'**🍻 CC:** {message.from_user.first_name}', reply_markup=but)
             await video.reply_video(out, caption=f'**✅ UPLOADED SUCCESSFULLY.**\n**🛠️ Engine:** `FFMAPG`\n**🚦 Preset:** `Ultrafast`\n**⚙️ CRF:** `{crf}`\n**📺 Quality:** `Standard`\n'
               + f'**🍻 CC:** {message.from_user.mention()}')
             os.remove(f'{file}')
             temp.pop(0)
             await f.delete()
          except Exception as a:
             os.remove(videox)
             temp.pop(0)
             await f.edit(f'**ERROR!:**\n`{a}`')
             return
   #    except Exception as a:
     #        await f.edit(f'**PROSESS ERROR ‼️:** `{a}`')
     #        return
             
@shakida.on_callback_query(
    filters.regex(pattern=r"cl")
)
async def callb(shakida, cb):
 #   chet_id = cb.message.chat.id
    global temp
    cbd = cb.data.strip()
    typed_=cbd.split(None, 1)[1]
    try:
       file, crf, any= typed_.split("|")
    except Exception as e:
       print(e)
       return
  #  sudo = int(875645659)
    useer_id = int(any)
  #  if cb.from_user.id != sudo:
    #    print('not sudo')    
    if cb.from_user.id != useer_id:
        await cb.answer("❌ Not for you.", show_alert=True)
        return
    try:
       try:
          os.remove(f'downloads/{file}')
       except:
          pass
       try:
          os.remove(f'{file}')
       except:
          pass
       temp.pop(0)
       bu = InlineKeyboardMarkup([[
                      InlineKeyboardButton("⚙️ Status", callback_data=f"sys"),
               ]])
       await cb.message.edit(f'**❌ STOPPED OPERATION**\n**⚙️ CRF RANGE:** {crf}\n'
       + f'**🍻 CC:** {cb.from_user.mention()}',
       reply_markup=bu)
    except Exception as e:
       await cb.message.edit(f'**Nothing to stopped ‼️**\n**Resion: `{e}`')
       return
@shakida.on_callback_query(filters.regex(pattern=r"^(sys)$"))
async def sya(shakida, cb):
     global temp
     list = len(temp)
     type_ = cb.matches[0].group(1)
   #   the_data = cb.message.reply_markup.inline_keyboard[1][0].callback_data
   #  by = cb.from_user.first_name
   #  userr = cb.from_user.id
     if type_ == "sys":
      #    await cb.answer(f"❌ Close by {by}")
      #    LOGGER.warning("Close button executed")
          ccpu = f"{psutil.cpu_percent(interval=1)}%"
          await cb.answer(f"💡 OPERATION STATUS:\n\n⚙️ Cpu usage: {ccpu}\n🗜️ #{list} Running 🟢", show_alert=True)
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


async def generate_sysinfo(workdir):
    # uptime
    info = {}
    info["🔌boot"] = datetime.fromtimestamp(psutil.boot_time()).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    # CPU
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    info["🌡️cpu"] = (
        f" {psutil.cpu_percent(interval=1)}% " f"({psutil.cpu_count()}) " f"{cpu_freq}"
    )
    # Memory
    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()
    info["💾ram"] = f"{bytes2human(vm.total)}, " f"{bytes2human(vm.available)} available"
    info["💽swap"] = f"{bytes2human(sm.total)}, {sm.percent}%"
    # Disks
    du = psutil.disk_usage(workdir)
    dio = psutil.disk_io_counters()
    info["💿disk"] = (
        f"{bytes2human(du.used)} / {bytes2human(du.total)} " f"({du.percent}%)"
    )
    if dio:
        info["📀disk io"] = (
            f"R {bytes2human(dio.read_bytes)} | " f"W {bytes2human(dio.write_bytes)}"
        )
    # Network
    nio = psutil.net_io_counters()
    info["🚀net io"] = (
        f"TX {bytes2human(nio.bytes_sent)} | " f"RX {bytes2human(nio.bytes_recv)}"
    )
    # Sensors
    sensors_temperatures = psutil.sensors_temperatures()
    if sensors_temperatures:
        temperatures_list = [x.current for x in sensors_temperatures["coretemp"]]
        temperatures = sum(temperatures_list) / len(temperatures_list)
        info["🌡️temp"] = f"{temperatures}\u00b0C"
    info = {f"{key}:": value for (key, value) in info.items()}
    max_len = max(len(x) for x in info)
    return "```" + "\n".join([f"{x:<{max_len}} {y}" for x, y in info.items()]) + "```"
    """
    partition_info = []
    for part in psutil.disk_partitions():
        mp = part.mountpoint
        du = psutil.disk_usage(mp)
        partition_info.append(f"{part.device} {mp} "
                              f"{part.fstype} "
                              f"{du.used} / {du.total} {du.percent}")
    partition_info = ",".join(partition_info)
    """


@shakida.on_message(filters.command("cmsys") & filters.group)
async def get_sysinfo(client: shakida, m):
    response = "⚙️ __**System Information:**__\n"
    m_reply = await m.reply_text(f"{response}`...`")
    response += await generate_sysinfo(client.workdir)
    await m_reply.edit_text(response)



idle()
