from mythic_container.PayloadBuilder import *
from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *


class SMB(PayloadType):
    name = "smb"
    file_extension = ""
    author = "Spencer Adolph"
    supported_os = [
        SupportedOS.Windows
    ]
    wrapper = False
    wrapped_payloads = []
    note = "This payload connects to smb."
    supports_dynamic_loading = False
    mythic_encrypts = False
    translation_container = None
    agent_path = pathlib.Path(".") / "smb_agent"
    agent_icon_path = agent_path / "agent_functions" / "smb.svg"
    agent_code_path = agent_path / "agent_code"
    c2_profiles = []
    build_parameters = [
        BuildParameter(
            name="host",
            parameter_type=BuildParameterType.String,
            default_value="127.0.0.1",
            description="Host to connect to.",
            required=True
        ),
        BuildParameter(
            name="username",
            parameter_type=BuildParameterType.String,
            default_value="Administrator",
            description="Username to use during authentication.",
            required=True
        ),
        # TODO: add 'domain' as an optional build parameter for domain joined machines
        BuildParameter(
            name="password",
            parameter_type=BuildParameterType.String,
            default_value="password",
            description="Password to use during authentication.",
            required=True
        ),
    ]

    async def build(self) -> BuildResponse:
        resp = BuildResponse(
            status=BuildStatus.Success,
        )
        return resp
    
    async def on_new_callback(self, newCallback: PTOnNewCallbackAllData) -> PTOnNewCallbackResponse:
        # create the smb connection in the background
        payload_uuid = newCallback.Payload.UUID
        connect_ip = self.get_parameter('host')
        username = self.get_parameter('username')
        password = self.get_parameter('password')
        
        # output, errors = await connect_to_smb(payload_uuid, username, password, connect_ip)

        return PTOnNewCallbackResponse(AgentCallbackID=newCallback.Callback.AgentCallbackID, Success=True)
