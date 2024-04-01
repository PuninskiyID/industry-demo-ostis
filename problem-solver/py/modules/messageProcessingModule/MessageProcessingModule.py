from sc_kpm import ScModule
from .ExampleAgent import ExampleAgent


class MessageProcessingModule(ScModule):
    def __init__(self):
        super().__init__(ExampleAgent())
