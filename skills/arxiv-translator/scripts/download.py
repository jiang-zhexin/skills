# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "seedir>=0.5.1",
# ]
# ///
import shutil
import sys
import tarfile
import tempfile
from urllib.request import urlopen

import seedir as sd


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: uv run download.py <arxiv_id>", file=sys.stderr)
        sys.exit(1)

    arxiv_id = sys.argv[1]

    with tempfile.NamedTemporaryFile(suffix=".tar.gz") as tmp:
        with urlopen(f"https://arxiv.org/src/{arxiv_id}") as resp:
            shutil.copyfileobj(resp, tmp)
        tmp.seek(0)

        dest_dir = tempfile.mkdtemp(prefix=f"arxiv-translator-{arxiv_id}-")
        with tarfile.open(fileobj=tmp, mode="r:*") as tar:
            tar.extractall(dest_dir, filter="data")

    print("success download:", dest_dir)
    print("the dir tree:")
    sd.seedir(dest_dir, exclude_files=[r".*\.pdf$", r".*\.png$"], regex=True)


if __name__ == "__main__":
    main()
