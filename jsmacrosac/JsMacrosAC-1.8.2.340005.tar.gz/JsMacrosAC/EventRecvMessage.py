from typing import overload
from typing import List
from typing import TypeVar
from .BaseEvent import BaseEvent
from .TextHelper import TextHelper

MessageIndicator = TypeVar["net.minecraft.client.gui.hud.MessageIndicator"]
MessageSignatureData = TypeVar["net.minecraft.network.message.MessageSignatureData"]
Text = TypeVar["net.minecraft.text.Text"]

class EventRecvMessage(BaseEvent):
	"""
	Since: 1.2.7 
	"""
	text: TextHelper
	signature: List[float]
	messageType: str

	@overload
	def __init__(self, message: Text, signature: MessageSignatureData, indicator: MessageIndicator) -> None:
		pass

	@overload
	def toString(self) -> str:
		pass

	pass


