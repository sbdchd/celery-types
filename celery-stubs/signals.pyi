from celery.utils.dispatch import Signal

__all__ = [
    "before_task_publish",
    "after_task_publish",
    "task_prerun",
    "task_postrun",
    "task_success",
    "task_retry",
    "task_failure",
    "task_revoked",
    "celeryd_init",
    "celeryd_after_setup",
    "worker_init",
    "worker_process_init",
    "worker_ready",
    "worker_shutdown",
    "worker_shutting_down",
    "setup_logging",
    "after_setup_logger",
    "after_setup_task_logger",
    "beat_init",
    "beat_embedded_init",
    "heartbeat_sent",
    "eventlet_pool_started",
    "eventlet_pool_preshutdown",
    "eventlet_pool_postshutdown",
    "eventlet_pool_apply",
]

before_task_publish: Signal
after_task_publish: Signal
task_received: Signal
task_prerun: Signal
task_postrun: Signal
task_success: Signal
task_retry: Signal
task_failure: Signal
task_revoked: Signal
task_rejected: Signal
task_unknown: Signal
#: Deprecated, use after_task_publish instead.
task_sent: Signal

celeryd_init: Signal
celeryd_after_setup: Signal

import_modules: Signal
worker_init: Signal
worker_process_init: Signal
worker_process_shutdown: Signal
worker_ready: Signal
worker_shutdown: Signal
worker_shutting_down: Signal
heartbeat_sent: Signal

setup_logging: Signal
after_setup_logger: Signal
after_setup_task_logger: Signal

beat_init: Signal
beat_embedded_init: Signal

eventlet_pool_started: Signal
eventlet_pool_preshutdown: Signal
eventlet_pool_postshutdown: Signal
eventlet_pool_apply: Signal

user_preload_options: Signal
