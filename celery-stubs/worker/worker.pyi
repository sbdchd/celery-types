from .components import Timer, Hub, Pool

class WorkController:
    hub: Hub | None
    pool: Pool | None
    timer: Timer | None
