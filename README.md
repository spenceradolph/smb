# SMB

An smb (wrapper) agent for Mythic. Great for LOTL.

### Local Development

```bash
sudo apt install cifs-utils

git clone https://github.com/spenceradolph/smb
cd smb

python3 -m venv ./.venv
source ./.venv/bin/activate
pip install mythic_container impacket
python3 ./Payload_Type/smb_agent/main.py
```
