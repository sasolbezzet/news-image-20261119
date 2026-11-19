import os, shutil

def run():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(src, os.path.join(out, "entry.png"))

if __name__ == "__main__":
    run()
