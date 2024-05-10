from sc_kpm import ScModule
from .ExampleAgent import ExampleAgent
from .VoiseAssistantAgent import VoiseAssistantAgent



class MessageProcessingModule(ScModule):
    def __init__(self):
        super().__init__(ExampleAgent())
        super().__init__(VoiseAssistantAgent())
        
