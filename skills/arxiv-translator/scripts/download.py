# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
import shutil
import sys
import tarfile
import tempfile
from urllib.request import urlopen


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


if __name__ == "__main__":
    main()
