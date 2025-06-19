# Clipboard Translator

A lightweight, discreet Python utility that translates text directly from your clipboard using Google Translate. Perfect for students, researchers, or anyone who needs quick translations without switching between applications.

## Features

- 🚀 **Instant Translation**: Translates clipboard content with a single keystroke
- 🔄 **Auto-detect Source Language**: Automatically detects the input language
- ⚙️ **Configurable**: Easy-to-modify settings file for target language preferences
- 🤫 **Discreet Operation**: No visible UI - works silently in the background
- 📋 **Seamless Workflow**: Results are automatically copied back to clipboard

## How It Works

1. Copy any text to your clipboard
2. Trigger the script (via keyboard shortcut)
3. The translated text automatically replaces your clipboard content
4. Paste anywhere you need the translation

## Installation

### Prerequisites

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install xclip
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install xclip
```

**macOS:**
```bash
# xclip not needed on macOS
```

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ha1fdan/clipboard-translator.git
   cd clipboard-translator
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your preferences** (optional):
   Edit `settings.conf` to set your preferred target language:
   ```
   DESTINATION_LANG=de  # German (change to your preferred language code)
   SRC_LANG=auto        # Auto-detect source language
   ```

## Configuration

### Language Codes

Common language codes you can use in `settings.conf`:

| Language | Code |
|----------|------|
| English | `en` |
| German | `de` |
| French | `fr` |
| Spanish | `es` |
| Italian | `it` |
| Portuguese | `pt` |
| Russian | `ru` |
| Japanese | `ja` |
| Chinese (Simplified) | `zh` |
| Korean | `ko` |

For a complete list of supported languages, run:
```python
from googletrans import LANGUAGES
print(LANGUAGES)
```

## Usage

### Command Line
```bash
python main.py
```

### Keyboard Shortcut (Recommended)

Setting up a keyboard shortcut makes the tool much more convenient:

#### Pop!_OS / Ubuntu (GNOME)
1. Open **Settings** → **Keyboard** → **Keyboard Shortcuts**
2. Click **+** to add a custom shortcut
3. **Name**: `Clipboard Translator`
4. **Command**: `/usr/bin/python3 /path/to/clipboard-translator/main.py`
5. **Shortcut**: Choose your preferred key combination (e.g., `Ctrl+Shift+T`)

#### Other Linux Distributions
Refer to your desktop environment's documentation for setting up custom keyboard shortcuts.

#### Windows
Use AutoHotkey or similar tools to bind the script to a keyboard shortcut.

#### macOS
Use Automator or Alfred to create a keyboard shortcut.

## Example Workflow

1. **Copy text**: Select and copy text like `"Hello, how are you?"`
2. **Press shortcut**: Hit your configured keyboard shortcut (e.g., `Ctrl+Shift+T`)
3. **Paste translation**: The clipboard now contains `"Hallo, wie geht es dir?"` (if translating to German)

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'googletrans'"**
```bash
pip install googletrans==4.0.0-rc1
```

**"ModuleNotFoundError: No module named 'pyperclip'"**
```bash
pip install pyperclip
```

**Linux clipboard issues:**
- Make sure `xclip` is installed
- Try running `xclip -version` to verify installation

**Translation not working:**
- Check your internet connection (Google Translate API requires internet)
- Verify language codes in `settings.conf` are valid

### Debug Mode

To see what's happening, you can modify `main.py` to add debug output:
```python
print(f"Original text: {text_to_translate}")
print(f"Translated text: {translated_text}")
```

## Dependencies

- `googletrans==4.0.0-rc1` - Google Translate API wrapper
- `pyperclip` - Cross-platform clipboard access

## Disclaimer

This tool uses the unofficial Google Translate API. For production use or high-volume translations, consider using the official Google Cloud Translation API.

---

**Made with ❤️ for seamless translation workflows**
