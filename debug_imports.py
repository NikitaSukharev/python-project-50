import sys
import os

print("=" * 50)
print("DIAGNOSTIC INFORMATION")
print("=" * 50)
print(f"\nCurrent directory: {os.getcwd()}")
print(f"\nDirectory contents:")
os.system("ls -la")
print(f"\nPython path:")
for p in sys.path:
    print(f"  - {p}")
print(f"\n'gendiff' directory exists: {os.path.exists('gendiff')}")
print(f"'gendiff/__init__.py' exists: {os.path.exists('gendiff/__init__.py')}")
try:
    import gendiff
    print(f"\n✓ Successfully imported gendiff from: {gendiff.__file__}")
except ModuleNotFoundError as e:
    print(f"\n✗ Failed to import gendiff: {e}")
