#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

_CONFIGURED = False


def _resolve_log_level() -> int:
	level_name = os.getenv("TF_LOG_LEVEL", "INFO").upper()
	return getattr(logging, level_name, logging.INFO)


def setup_logging(log_dir: str = "log", log_file_name: str = "testflow.log") -> logging.Logger:
	"""Configure project logging with console and rotating file handlers."""
	global _CONFIGURED

	logger = logging.getLogger("testflow")
	if _CONFIGURED:
		return logger

	os.makedirs(log_dir, exist_ok=True)
	log_file_path = os.path.join(log_dir, log_file_name)

	max_bytes = int(os.getenv("TF_LOG_MAX_BYTES", str(5 * 1024 * 1024)))
	backup_count = int(os.getenv("TF_LOG_BACKUP_COUNT", "5"))
	log_level = _resolve_log_level()

	formatter = logging.Formatter(
		fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
		datefmt="%Y-%m-%d %H:%M:%S",
	)

	file_handler = RotatingFileHandler(
		log_file_path,
		maxBytes=max_bytes,
		backupCount=backup_count,
		encoding="utf-8",
	)
	file_handler.setFormatter(formatter)

	console_handler = logging.StreamHandler(stream=sys.stdout)
	console_handler.setFormatter(formatter)

	logger.setLevel(log_level)
	logger.addHandler(file_handler)
	logger.addHandler(console_handler)
	logger.propagate = False

	_CONFIGURED = True
	logger.info(
		"Logging initialized: dir=%s file=%s max_bytes=%s backups=%s level=%s",
		log_dir,
		log_file_name,
		max_bytes,
		backup_count,
		logging.getLevelName(log_level),
	)
	return logger


def get_logger(name: str) -> logging.Logger:
	setup_logging()
	return logging.getLogger(f"testflow.{name}")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="LogManager debug entry")
	parser.add_argument("--dir", dest="log_dir", default="log", help="Log directory")
	parser.add_argument("--file", dest="log_file", default="testflow.log", help="Log file name")
	parser.add_argument(
		"--level",
		dest="log_level",
		default=os.getenv("TF_LOG_LEVEL", "INFO"),
		help="Log level (DEBUG/INFO/WARNING/ERROR)",
	)
	parser.add_argument("--message", dest="message", default="log_manager main test", help="Test message")
	args = parser.parse_args()

	os.environ["TF_LOG_LEVEL"] = str(args.log_level)
	setup_logging(log_dir=args.log_dir, log_file_name=args.log_file)

	logger = get_logger("main")
	logger.debug("debug: %s", args.message)
	logger.info("info: %s", args.message)
	logger.warning("warning: %s", args.message)
	logger.error("error: %s", args.message)
