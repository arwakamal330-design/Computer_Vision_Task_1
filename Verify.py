#!/usr/bin/env python3

import importlib

# Package name : Module name
libraries = {
    "opencv-python": "cv2",
    "numpy": "numpy",
    "Pillow": "PIL",
    "matplotlib": "matplotlib"
}

print("=" * 50)
print("Python Library Installation Verification")
print("=" * 50)

all_installed = True

for package_name, module_name in libraries.items():
    try:
        module = importlib.import_module(module_name)

        # Try to get version
        version = getattr(module, "__version__", "Version unavailable")

        print(f"✓ {package_name:<18} Installed (Version: {version})")
    except ImportError:
        print(f"✗ {package_name:<18} NOT Installed")
        all_installed = False

print("=" * 50)

if all_installed:
    print("✅ All required libraries are installed.")
else:
    print("❌ Some libraries are missing.")
    print("\nInstall the missing libraries with:")
    print("pip install opencv-python numpy Pillow matplotlib")

print(f"\nPython Version: {__import__('sys').version.split()[0]}")