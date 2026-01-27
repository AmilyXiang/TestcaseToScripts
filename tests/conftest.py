from __future__ import annotations

import os
from dataclasses import dataclass

import pytest
import yaml


@dataclass
class SshResult:
    command: str
    exit_code: int
    stdout: str
    stderr: str


class SshSession:
    def __init__(self, host: str, user: str, password: str | None, port: int = 22, key_path: str | None = None):
        import paramiko

        self._paramiko = paramiko
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        connect_kwargs = {"hostname": host, "username": user, "port": port, "timeout": 30}
        if key_path:
            connect_kwargs["key_filename"] = key_path
        else:
            connect_kwargs["password"] = password

        self._client.connect(**connect_kwargs)

    def exec(self, command: str, timeout: int = 60) -> SshResult:
        stdin, stdout, stderr = self._client.exec_command(command, timeout=timeout)
        exit_code = stdout.channel.recv_exit_status()
        out = stdout.read().decode(errors="replace")
        err = stderr.read().decode(errors="replace")
        return SshResult(command=command, exit_code=exit_code, stdout=out, stderr=err)

    def close(self) -> None:
        self._client.close()


def _load_dut_config() -> dict:
    # Priority: env vars > dut.yaml (optional)
    cfg = {
        "host": os.environ.get("DUT_HOST"),
        "user": os.environ.get("DUT_USER"),
        "password": os.environ.get("DUT_PASSWORD"),
        "port": int(os.environ.get("DUT_PORT", "22")),
        "key_path": os.environ.get("DUT_KEY_PATH"),
    }

    dut_yaml = os.environ.get("DUT_YAML", "dut.yaml")
    if os.path.exists(dut_yaml):
        loaded = yaml.safe_load(open(dut_yaml, "r", encoding="utf-8")) or {}
        if isinstance(loaded, dict):
            for k in cfg:
                cfg[k] = cfg[k] or loaded.get(k)

    return cfg


@pytest.fixture(scope="session")
def ssh_session():
    cfg = _load_dut_config()
    if not cfg.get("host") or not cfg.get("user"):
        pytest.skip("DUT not configured. Set DUT_HOST/DUT_USER (and DUT_PASSWORD or DUT_KEY_PATH), or create dut.yaml")

    session = SshSession(
        host=str(cfg["host"]),
        user=str(cfg["user"]),
        password=str(cfg.get("password") or ""),
        port=int(cfg.get("port") or 22),
        key_path=str(cfg["key_path"]) if cfg.get("key_path") else None,
    )
    yield session
    session.close()


@pytest.fixture(scope="session")
def step_mapping_rules():
    import pathlib

    mapping_path = pathlib.Path(os.environ.get("STEP_MAPPING", "step_mapping.yaml"))
    if not mapping_path.exists():
        return []
    data = yaml.safe_load(mapping_path.read_text(encoding="utf-8")) or {}
    rules = data.get("rules", [])
    return rules if isinstance(rules, list) else []
