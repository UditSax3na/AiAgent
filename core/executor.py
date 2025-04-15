from config.constants import PROG_LANG, LANG_EXT, LANG_COM
from config.paths import OUTPUT_DIR, LOG_DIR
from pathlib import Path
import subprocess
import datetime
import traceback
import shutil
import re

def clean_code_block(code_str):
    cleaned = re.sub(r"```(?:\w+)?\s*", "", code_str)  # opening ```
    cleaned = re.sub(r"```", "", cleaned)              # closing ```
    cleaned = re.sub(r"[-]+$", "", cleaned).strip()
    return cleaned.strip()

def is_command_available(command):
    return shutil.which(command) is not None

def runCode(filepath_str):
    filepath = Path(filepath_str).resolve()
    ext = filepath.suffix
    print(f"this is extension : {ext}")

    cmd_template = LANG_COM.get(ext)
    if not cmd_template:
        print(f"Unsupported file extension: {ext}")
        return

    required_command = cmd_template[0].split()[0].replace("{filename}", "").strip()
    if not is_command_available(required_command):
        print(f"Required compiler/interpreter '{required_command}' is not installed or not in PATH.")
        return

    cmd = [arg.replace("{filename}", str(filepath)) for arg in cmd_template]

    try:
        subprocess.run(cmd, check=True)
        if ext in [".c", ".cpp"]:
            binary = Path(OUTPUT_DIR / 'a.out')
            if binary.exists():
                subprocess.run([str(binary)], check=True)
            else:
                raise FileNotFoundError("Compiled output 'a.out' not found.")

        elif ext == ".java":
            if not is_command_available("java"):
                raise FileNotFoundError("Java runtime not found.")
            class_name = filepath.stem
            subprocess.run(["java", class_name], check=True)

        elif ext == ".rs":
            binary = filepath.with_suffix("").name
            bin_path = Path(binary)
            if bin_path.exists():
                subprocess.run([f"./{binary}"], check=True)
            else:
                raise FileNotFoundError(f"Rust compiled output '{binary}' not found.")

    except subprocess.CalledProcessError as e:
        logfile = LOG_DIR / 'log.txt'
        with open(logfile, 'a') as myfile:  # Append mode
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_trace = traceback.format_exc()  # Full traceback
            myfile.write(f"[{timestamp}] Error: {str(e)}\n")
            myfile.write(f"[{timestamp}] Traceback:\n{error_trace}\n")
            myfile.write(f"[{timestamp}] File Location: {__file__}\n")
            myfile.write("-" * 60 + "\n")

def execTask(code):
    if code['language'] == "c++":
        code['language'] == "cpp"
    if code['language'] in PROG_LANG:
        ext = LANG_EXT[code['language']]
    else:
        return False, "Error! Code language is not specified"
    
    OUTPUT_FILE = Path(OUTPUT_DIR / f'task{ext}')
    if not OUTPUT_FILE.exists():
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    cleaned_code = clean_code_block(code['content'])
    OUTPUT_FILE.write_text(cleaned_code)

    runCode(OUTPUT_FILE)
    
    return True, "Task has been saved and executed successfully! \nNote: code can be found in (/output/task"+ext+")"
