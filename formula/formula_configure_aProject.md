# SonarQube Project Configuration Guide 📝

## Overview 🌟
This guide details setting up SonarQube with GitHub integration using GitHub Apps and Actions.

## Prerequisites ✅
- GitHub account with admin access
- Running SonarQube instance
- GitHub Developer Settings access
- GitHub Actions knowledge

## Configuration Steps 🔧

### 1. GitHub App Setup 🔑
1. Navigate to GitHub Developer Settings
2. Create/Configure `SonarQubeCourseApp`
3. Set permissions and webhook details
4. Install app on repository

### 2. SonarQube Setup 🖥️
1. Access SonarQube instance
2. Create project with key
3. Configure webhook

### 3. GitHub Actions Workflow ⚙️
Create `.github/workflows/sonarqube.yml`:
```yaml
name: Build
on:
    push:
        branches:
            - main
jobs:
    build:
        name: Build
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v2
                with:
                    fetch-depth: 0
            - uses: sonarsource/sonarqube-scan-action@master
                env:
                    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
                    SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

### 4. Secret Configuration 🔒
Add to repository secrets:
- `SONAR_TOKEN`
- `SONAR_HOST_URL`

### 5. Important Notes ⚠️
- Update URLs after Codespace restarts
- Verify webhook configurations
- Check permissions regularly

## Additional Resources
- Configuration: `obsidian://open?vault=secondbrain&file=secondbrain%2F4%20_Archieve%2Fresetup%20appid%20and%20config%20for%20sonarqube%20project%201%206%202025`
- Secrets management: `https://github.com/rifaterdemsahin/SonarQubeCourse/settings/secrets/actions`

## Troubleshooting 🛡️
- Verify webhook configurations
- Check GitHub Actions logs
- Confirm permissions
- Validate URLs after Codespace restarts
