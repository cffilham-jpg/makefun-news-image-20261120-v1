"""news-image-20261120 v1: copy the pre-rendered front page to the output dir.

The entry image is a dense broadsheet-style front page summing up the
world's news of Friday 20 November 2026: 36 verified stories, a hero band
with the ICJ genocide ruling and the Trump-Xi-Putin summit, a three-column
story grid, a markets strip and a source footer.

This program uses only the Python standard library. It copies entry.png
(the image shipped in this repository) into $MAKEFUN_OUTPUT_DIR and
checks the copy landed intact.
"""

import hashlib
import os
import shutil
import sys

ENTRY = "entry.png"
EXPECTED_SIZE = 198851


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY)
    dst = os.path.join(out_dir, ENTRY)
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    got = os.path.getsize(dst)
    if got != EXPECTED_SIZE:
        print(f"size mismatch: copied {got} bytes, expected {EXPECTED_SIZE}",
              file=sys.stderr)
        return 1
    src_hash = sha256_of(src)
    dst_hash = sha256_of(dst)
    if src_hash != dst_hash:
        print(f"sha256 mismatch: source {src_hash}, copy {dst_hash}",
              file=sys.stderr)
        return 1
    print(f"wrote {dst} ({got} bytes, sha256 {dst_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
