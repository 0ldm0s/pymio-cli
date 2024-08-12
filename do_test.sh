#!/usr/bin/env bash
export FLASK_APP=mio.shell
export MIO_CONFIG=production
export PYTHONUNBUFFERED=1
export PYTHONIOENCODING=utf-8
python -m flask cli exe -cls=cli.WorkMan.Daemon.do_test
