
import PIL.Image
import os
import sys

try:
    for f in os.listdir('output/plots'):
        if f.endswith('.png'):
            try:
                img = PIL.Image.open(os.path.join('output/plots', f))
                img.verify()
                print(f"Verified {f}: OK")
            except Exception as e:
                print(f"Verified {f}: FAILED - {e}")
except Exception as e:
    print(e)
