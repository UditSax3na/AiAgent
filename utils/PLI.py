import re

def splitResponse(text):
    heading_patterns = {
        "plan": re.compile(r"^(?:#+\s*)?(?:\d+\.\s*)?\**\s*plan\s*\**(?:\s*\(.*\))?\s*$", re.IGNORECASE),
        "code": re.compile(r"^(?:#+\s*)?(?:\d+\.\s*)?\**\s*code\s*\**(?:\s*\(.*\))?\s*$", re.IGNORECASE),
        "how to run": re.compile(r"^(?:#+\s*)?(?:\d+\.\s*)?\**\s*how to run\s*\**(?:\s*\(.*\))?\s*$", re.IGNORECASE),
    }

    lines = text.splitlines()
    sections = {}
    current_title = None
    buffer = []

    for line in lines:
        line_stripped = line.strip()
        matched_section = None

        for key, pattern in heading_patterns.items():
            if pattern.match(line_stripped):
                matched_section = key
                break

        if matched_section:
            if current_title and buffer:
                content = "\n".join(buffer)
                if current_title == "code":
                    code_match = re.search(r"```(\w+)?\n(.*?)```", content, re.DOTALL)
                    if code_match:
                        language = code_match.group(1) if code_match.group(1) else "unknown"
                        code_content = code_match.group(2).strip()
                        sections[current_title] = {
                            "language": language,
                            "content": code_content
                        }
                else:
                    sections[current_title] = content.strip()
                buffer = []
            current_title = matched_section
        elif current_title:
            buffer.append(line)

    # Final section check
    if current_title and buffer:
        content = "\n".join(buffer)
        if current_title == "code":
            code_match = re.search(r"```(\w+)?\n(.*?)```", content, re.DOTALL)
            if code_match:
                language = code_match.group(1) if code_match.group(1) else "unknown"
                code_content = code_match.group(2).strip()
                sections[current_title] = {
                    "language": language,
                    "content": code_content
                }
        else:
            sections[current_title] = content.strip()

    return sections