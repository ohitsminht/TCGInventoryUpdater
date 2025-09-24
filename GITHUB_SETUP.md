# GitHub Actions Setup Guide

This guide will help you set up GitHub Actions to automatically build and distribute your TCGPlayer Inventory Updater application.

## Prerequisites

1. A GitHub account
2. Your code pushed to a GitHub repository

## Step-by-Step Setup

### 1. Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name it `TCGInventoryUpdater` (or your preferred name)
5. Make it **Public** (required for free GitHub Actions)
6. Don't initialize with README (since you already have files)
7. Click "Create repository"

### 2. Upload Your Code

#### Option A: Using Git Command Line
```bash
# Navigate to your project folder
cd /Users/minhlam/TCGInventoryUpdater

# Initialize git repository
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: TCGPlayer Inventory Updater"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/TCGInventoryUpdater.git

# Push to GitHub
git push -u origin main
```

#### Option B: Using GitHub Web Interface
1. Go to your repository on GitHub
2. Click "uploading an existing file"
3. Drag and drop all your project files
4. Add commit message: "Initial commit: TCGPlayer Inventory Updater"
5. Click "Commit changes"

### 3. Verify GitHub Actions Workflow

1. Go to your repository on GitHub
2. Click the "Actions" tab
3. You should see "Build and Release TCGInventoryUpdater" workflow
4. If you don't see it, make sure the `.github/workflows/build.yml` file is in your repository

### 4. Test the Workflow

#### Option A: Manual Trigger (Recommended for testing)
1. Go to the "Actions" tab in your repository
2. Click on "Build and Release TCGInventoryUpdater"
3. Click "Run workflow" button
4. Select the branch (usually "main")
5. Click "Run workflow"

#### Option B: Create a Release Tag
```bash
# Create a version tag
git tag v1.0.0

# Push the tag to trigger the workflow
git push origin v1.0.0
```

### 5. Monitor the Build

1. Go to the "Actions" tab
2. Click on the running workflow
3. You'll see separate jobs for Windows and macOS
4. Wait for both to complete (usually 5-10 minutes)

### 6. Download Your Executables

Once the workflow completes successfully:

1. Go to the "Releases" section of your repository
2. You should see a new release with your version number
3. Download the appropriate executable for your platform:
   - `TCGInventoryUpdater-Windows.exe` for Windows
   - `TCGInventoryUpdater-macOS` for macOS

## Troubleshooting

### Common Issues

#### 1. Workflow Not Appearing
- Make sure the `.github/workflows/build.yml` file exists in your repository
- Check that the file is in the correct location: `.github/workflows/build.yml`

#### 2. Build Fails
- Check the Actions tab for error messages
- Common issues:
  - Missing dependencies
  - Python version compatibility
  - File path issues

#### 3. No Release Created
- Make sure you're using a version tag (v1.0.0, v1.1.0, etc.)
- Check that the workflow completed successfully

#### 4. Permission Issues
- Make sure your repository is public (GitHub Actions requires public repos for free accounts)
- Or upgrade to GitHub Pro for private repository actions

### Getting Help

1. Check the Actions tab for detailed error logs
2. GitHub Actions documentation: https://docs.github.com/en/actions
3. Create an issue in your repository if problems persist

## Updating Your Application

To create a new release with updates:

1. Make your changes to the code
2. Commit and push your changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```
3. Create a new version tag:
   ```bash
   git tag v1.1.0  # Increment version number
   git push origin v1.1.0
   ```
4. GitHub Actions will automatically build and create a new release

## Sharing with Friends

Once you have a release:

1. Go to your repository's "Releases" section
2. Copy the release URL
3. Share it with your friends
4. They can download the appropriate executable for their platform

## Security Note

The executables built by GitHub Actions are unsigned, which means:
- Windows may show a security warning (click "More info" → "Run anyway")
- macOS may show an "unidentified developer" warning (right-click → "Open")

This is normal for applications built without a code signing certificate.
