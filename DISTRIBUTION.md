# Distribution Guide for TCGPlayer Inventory Updater

This guide explains how to distribute the TCGPlayer Inventory Updater to your friends on both Windows and Mac.

## Distribution Methods

### Method 1: GitHub Actions (Recommended)

This is the most automated and professional approach:

#### Setup:
1. **Create a GitHub Repository**:
   - Go to GitHub and create a new repository
   - Upload all the application files
   - The repository already includes the GitHub Actions workflow

2. **Create a Release**:
   - Go to your repository on GitHub
   - Click "Releases" → "Create a new release"
   - Create a tag like `v1.0.0`
   - GitHub Actions will automatically build executables for both platforms

3. **Download and Share**:
   - After the build completes, download the executables from the release page
   - Share the release URL with your friends

#### Benefits:
- ✅ Automatic builds for both Windows and Mac
- ✅ Professional release management
- ✅ Easy updates (just create new releases)
- ✅ No need to manually build on each platform

### Method 2: Manual Building

If you prefer to build locally:

#### For macOS:
```bash
# Install PyInstaller
pip3 install pyinstaller

# Build the executable
python3 build_executable.py
```

#### For Windows:
```powershell
# Install PyInstaller
pip install pyinstaller

# Build the executable
python build_executable.py
```

### Method 3: Python Package Distribution

For users who have Python installed:

1. **Install from source**:
   ```bash
   git clone https://github.com/yourusername/TCGInventoryUpdater.git
   cd TCGInventoryUpdater
   pip install -e .
   ```

2. **Run the application**:
   ```bash
   tcg-inventory-updater
   ```

## File Structure for Distribution

```
TCGInventoryUpdater/
├── tcg_inventory_updater.py      # Main application
├── requirements.txt              # Dependencies
├── README.md                     # Documentation
├── DISTRIBUTION.md              # This file
├── build_executable.py          # Build script
├── setup.py                     # Package setup
├── .github/workflows/build.yml  # GitHub Actions workflow
├── sample_main_inventory.csv    # Sample files
├── sample_addition1.csv
└── sample_addition2.csv
```

## User Instructions

### For Windows Users:
1. Download `TCGInventoryUpdater-Windows.exe`
2. Double-click to run (no installation required)
3. If Windows Defender warns about unknown publisher, click "More info" → "Run anyway"

### For Mac Users:
1. Download `TCGInventoryUpdater-macOS`
2. Right-click the file → "Open" (first time only, to bypass security warning)
3. Or run from Terminal: `chmod +x TCGInventoryUpdater-macOS && ./TCGInventoryUpdater-macOS`

## Troubleshooting

### Common Issues:

1. **"App can't be opened because it's from an unidentified developer" (Mac)**:
   - Right-click the app → "Open" → "Open" again
   - Or go to System Preferences → Security & Privacy → Allow the app

2. **Windows Defender warning**:
   - Click "More info" → "Run anyway"
   - Or add an exception in Windows Defender

3. **Missing dependencies**:
   - The executables should include all dependencies
   - If issues persist, try the Python package method

### Performance Tips:
- The application is optimized for responsiveness
- Large CSV files (>10,000 rows) may take a few seconds to process
- Use "Preview Changes" before applying updates

## Version Management

### Creating New Releases:
1. Update version numbers in relevant files
2. Create a new Git tag: `git tag v1.1.0`
3. Push the tag: `git push origin v1.1.0`
4. GitHub Actions will automatically build and create a release

### Updating the Application:
- Notify users about new releases
- Provide changelog with new features/fixes
- Consider backward compatibility with CSV file formats

## Support

### For Users:
- Share the README.md file with detailed usage instructions
- Include sample CSV files for testing
- Provide this distribution guide for setup help

### For Developers:
- Monitor GitHub Issues for bug reports
- Update documentation with new features
- Test on both platforms before releasing

## Security Considerations

- The executables are unsigned (no code signing certificate)
- Users may see security warnings on first run
- Consider getting a code signing certificate for professional distribution
- Scan executables with antivirus software before distribution

## Alternative Distribution Platforms

Consider these platforms for wider distribution:
- **GitHub Releases** (current method)
- **Microsoft Store** (Windows)
- **Mac App Store** (macOS)
- **Homebrew** (macOS command line)
- **Chocolatey** (Windows package manager)

Each platform has specific requirements and approval processes.
