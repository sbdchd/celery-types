from celery import bootsteps

class Timer(bootsteps.Step): ...
class Hub(bootsteps.StartStopStep): ...
class Pool(bootsteps.StartStopStep): ...
class Beat(bootsteps.StartStopStep): ...
class StateDB(bootsteps.Step): ...
class Consumer(bootsteps.StartStopStep): ...
