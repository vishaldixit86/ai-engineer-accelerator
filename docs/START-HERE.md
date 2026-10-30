# Start here — first 20 minutes as an AI Engineer

## Requirements
Git, Python 3.11+, your approved project repository, and (optionally) VS Code with GitHub Copilot. The tool is local and uses Python's standard library.

## Step 1: clone
```powershell
git clone https://github.com/vishaldixit86/ai-engineer-accelerator.git
cd ai-engineer-accelerator
```

## Step 2: find a use case
```powershell
python scripts/ai_engineer.py search fincrime
python scripts/ai_engineer.py list
```

## Step 3: install into your *separate*, authorized project
```powershell
python scripts/ai_engineer.py install --project C:\Projects\my-app --pack graphrag --dry-run
python scripts/ai_engineer.py install --project C:\Projects\my-app --pack graphrag
```

If the installer reports a collision, review it instead of force-overwriting. The installed project receives discoverable agents/skills where available and local governance guides. It does not install a remote LLM or execute agents automatically.

## Step 4: begin with a small task
Open your application workspace in VS Code. Select an available AI Engineer agent or ask your existing Copilot assistant:

> Inspect this repository. Explain the core files and call flow, identify the tests and permissions relevant to my task, then propose a scoped implementation and risks. Do not change code until I review the plan.

## Step 5: verify
After editing, run project-specific tests, record decisions and update the call flow when appropriate. Never equate generated test descriptions with executed tests.

## Data boundaries
All project context, private documents, evaluations and graph indexes stay in the project’s authorized environment. Do not open a PR to this public library containing client information.
