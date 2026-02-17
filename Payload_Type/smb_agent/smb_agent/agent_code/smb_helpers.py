from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *
import os

async def connect_to_smb(payload_uuid: str, connect_ip: str, domain: str, username: str, password: str):
    # add a mount for file transfer ease
    os.mkdir(f"/mnt/smb_{payload_uuid}.cifs")
    
    # TODO: use subprocess to get stdout and stderr to check for errors with the mount
    if domain == "":
        os.system(f"mount -t cifs -o username={username},password='{password}' //{connect_ip}/C$ /mnt/smb_{payload_uuid}.cifs")
    else:
        os.system(f"mount -t cifs -o username={username},password='{password}',domain={domain} //{connect_ip}/C$ /mnt/smb_{payload_uuid}.cifs")

    return


async def exit_smb(taskData: MythicCommandBase.PTTaskMessageAllData):
    payload_uuid = taskData.Payload.UUID

    # rm the smb mount
    os.system(f"umount /mnt/smb_{payload_uuid}.cifs")
    os.rmdir(f"/mnt/smb_{payload_uuid}.cifs")
    
    return

