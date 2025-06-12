import datetime
import yaml
import requests
import re
from pathlib import Path

RE_DOMAIN = re.compile(r"^[|@]*\|\|([^/^$]*)")
RE_SIMPLE_DOMAIN = re.compile(r"^[A-Za-z0-9.-]+$")

BLOCKLIST_SUFFIX = "_Blocklist.txt"
ALLOWLIST_SUFFIX = "_Allowlist.txt"


def is_valid_domain(domain: str) -> bool:
    """Simple domain validation."""
    if not domain:
        return False
    if domain.endswith('.'):
        domain = domain[:-1]
    if '..' in domain:
        return False
    if len(domain) > 253:
        return False
    if '.' not in domain:
        return False
    return bool(RE_SIMPLE_DOMAIN.match(domain))


def parse_domains(text):
    domains = set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("!") or line.startswith("#"):
            continue
        if line.startswith("@@||"):
            domain = RE_DOMAIN.match(line)
            if domain and is_valid_domain(domain.group(1)):
                domains.add(domain.group(1))
        elif line.startswith("||"):
            domain = RE_DOMAIN.match(line)
            if domain and is_valid_domain(domain.group(1)):
                domains.add(domain.group(1))
        elif line.startswith("0.0.0.0") or line.startswith("127.0.0.1"):
            parts = line.split()
            if len(parts) >= 2 and is_valid_domain(parts[1]):
                domains.add(parts[1])
    return domains


def extract_header(text):
    lines = []
    for line in text.splitlines():
        if line.startswith("!") or not line.strip():
            lines.append(line)
        else:
            break
    return lines


def update_list(path, sources, allow_domains):
    if path.endswith(ALLOWLIST_SUFFIX):
        print(f"Skipping update for allowlist {path}")
        return
    current_text = Path(path).read_text()
    header = extract_header(current_text)

    domains = parse_domains(current_text)

    for url in sources:
        try:
            if not url.startswith("http"):
                print(f"Skipping invalid URL {url}")
                continue
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                parsed = parse_domains(r.text)
                if not parsed:
                    print(f"No domains found in {url}")
                else:
                    domains.update(parsed)
            else:
                print(f"Unexpected status {r.status_code} for {url}")
        except Exception as e:
            print(f"Failed fetching {url}: {e}")

    # remove allowlist domains
    domains.difference_update(allow_domains)

    # sort domains
    sorted_domains = sorted(domains)

    # update last updated line
    today = datetime.date.today().isoformat()
    new_header = []
    last_updated_line_found = False
    for line in header:
        if line.startswith("! Last updated:"):
            new_header.append(f"! Last updated: {today}")
            last_updated_line_found = True
        else:
            new_header.append(line)
    if not last_updated_line_found:
        new_header.append(f"! Last updated: {today}")

    content = "\n".join(new_header) + "\n" + "\n".join(f"||{d}^" for d in sorted_domains) + "\n"
    Path(path).write_text(content)


def main():
    cfg_path = Path("sources.yml")
    if not cfg_path.exists():
        print("sources.yml not found; nothing to do")
        return
    cfg = yaml.safe_load(cfg_path.read_text())

    allow_domains = set()
    for allow_file in Path('.').glob(f'*{ALLOWLIST_SUFFIX}'):
        allow_domains.update(parse_domains(Path(allow_file).read_text()))

    for block_file, urls in cfg.items():
        if not block_file.endswith(BLOCKLIST_SUFFIX):
            print(f"Skipping unknown file {block_file}")
            continue
        if not Path(block_file).exists():
            print(f"Blocklist file {block_file} not found")
            continue
        if not isinstance(urls, list):
            urls = [urls]
        update_list(block_file, urls, allow_domains)


if __name__ == '__main__':
    main()
