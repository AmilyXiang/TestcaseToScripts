# TestcaseToScripts

## Fetch TestRail Auto Cases

This project supports pulling TestRail Auto cases and writing two JSON outputs:

- summary: `<output_prefix>.summary.json`
- details: `<output_prefix>.details.json`

Default output folder:

- `output_copilot/`

### 1) Recommended (Copilot CLI generator)

Use this first. It uses the prompt flow defined in `prompt/prompt.testrail_auto_cases_fetcher.md`.

#### By project

```powershell
d:/TestcaseToScripts/TestcaseToScripts/.venv/Scripts/python.exe d:/TestcaseToScripts/TestcaseToScripts/copilot-cli/generator_testrail_auto_cases_copilot.py --scope project --project-id 5 --output-dir output_copilot --output-prefix testrail_project_5_auto_cases
```

#### By run

```powershell
d:/TestcaseToScripts/TestcaseToScripts/.venv/Scripts/python.exe d:/TestcaseToScripts/TestcaseToScripts/copilot-cli/generator_testrail_auto_cases_copilot.py --scope run --run-id 36926 --output-dir output_copilot --output-prefix testrail_run_36926_auto_cases
```

### 2) Fallback (direct fetch script)

If Copilot CLI blocks/hangs in your environment, use this direct script:

```powershell
d:/TestcaseToScripts/TestcaseToScripts/.venv/Scripts/python.exe d:/TestcaseToScripts/TestcaseToScripts/tmp/fetch_project_auto_cases.py --project-id 5 --output-dir output_copilot --output-prefix testrail_project_5_auto_cases
```

### Output examples

- `output_copilot/testrail_project_5_auto_cases.summary.json`
- `output_copilot/testrail_project_5_auto_cases.details.json`

### Quick checklist

- Ensure `.vscode/mcp.json` contains valid TestRail credentials.
- Run inside project root: `d:/TestcaseToScripts/TestcaseToScripts`.
- Prefer explicit `--output-prefix` to avoid confusion.
