from sc_kpm import ScModule
from .CheckNodeAgent import CheckNodeAgent


class CheckModule(ScModule):
    def __init__(self):
        super().__init__(CheckNodeAgent())
