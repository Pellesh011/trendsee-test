# run_alembic.py
from alembic.config import CommandLine, Config
from alembic import command
cfg = Config("alembic.ini")
command.upgrade(cfg, "head")
