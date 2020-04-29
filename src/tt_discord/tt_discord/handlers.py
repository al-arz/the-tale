
from tt_web import handlers

from tt_protocol.protocol import discord_pb2

# from . import protobuf
# from . import operations


@handlers.api(discord_pb2.DebugClearServiceRequest)
async def debug_clear_service(message, **kwargs):
    await operations.clean_database()
    return discord_pb2.DebugClearServiceResponse()
