# Neko Run

A Chrome-dino style pixel cat runner by the Nekomo community. Dodge cucumbers and crows, grab fish, and chase a high score.

The same game runs on the [Nekomo website 404 page](https://nekomoapp.netlify.app/404) (open any missing page), as a Windows / Linux desktop app, and as an Android app.

## Download

Grab the latest build from [Releases](https://github.com/Nekomo-App/Neko-Run/releases/latest):

| Platform | File | Notes |
| --- | --- | --- |
| Windows (installer) | `Neko-Run-Setup-<version>.exe` | Start menu + desktop shortcut. Unsigned, so SmartScreen may ask: *More info → Run anyway* |
| Windows (portable) | `Neko-Run-<version>-portable.exe` | No install, just run it |
| Android | `Neko-Run-<version>.apk` | Android 7.0+. Allow *Install unknown apps* for your browser / file manager |
| Linux (AppImage) | `Neko-Run-<version>-x86_64.AppImage` | `chmod +x` it and run |
| Windows (zip) | `Neko-Run-<version>-win.zip` | Unzip anywhere and run `Neko Run.exe` |
| Linux (Debian/Ubuntu) | `neko-run_<version>_amd64.deb` | `sudo apt install ./neko-run_<version>_amd64.deb` |
| Linux (Fedora/openSUSE) | `neko-run-<version>.x86_64.rpm` | `sudo dnf install ./neko-run-<version>.x86_64.rpm` |
| Linux (tarball) | `Neko-Run-<version>-linux-x64.tar.gz` | Extract and run `neko-run` |

`SHA256SUMS.txt` in each release lists the checksum of every file.

Website page: https://nekomoapp.netlify.app/neko-run

## Packages

Each published release also pushes the web game to [GitHub Packages](https://github.com/orgs/Nekomo-App/packages?repo_name=Neko-Run) (`.github/workflows/packages.yml`):

| Package | Use it |
| --- | --- |
| npm: `@nekomo-app/neko-run` | Add `@nekomo-app:registry=https://npm.pkg.github.com` to `.npmrc`, then `npm install @nekomo-app/neko-run` and load `node_modules/@nekomo-app/neko-run/neko-run.js` |
| Container: `ghcr.io/nekomo-app/neko-run` | `docker run -p 8080:80 ghcr.io/nekomo-app/neko-run` and open http://localhost:8080 |

The npm package and the image version follow `web/package.json`. Keep it in step with `desktop/package.json` when you bump the version.

## How to play

| Action | Keyboard | Touch |
| --- | --- | --- |
| Jump (hold for higher) | Space / ↑ / W | Tap the game or **Jump** |
| Duck / fast fall | ↓ / S | **Duck** |
| Pause | P | Pause button |
| Mute | M | Speaker button |
| Full screen | F (or F11 in the desktop app) | Full screen button |
| Settings | gear button, Esc closes | gear button |

Fish are worth +25. On the website the game switches to full screen by itself after about 12 seconds of play (you can turn that off in settings).

### Settings

Sound, volume, difficulty (Easy / Normal / Hard, separate high scores), cat colour (Snow, Sakura, Ginger, Smoke, Midnight), sky (Sakura / Night), clouds/petals/stars effects, auto full screen, touch buttons (Auto / On / Off) and a high-score reset. Everything is saved on the device.

## Project layout

```
web/        the game: neko-run.js (engine, no dependencies), index.html (app shell), fonts, icon
desktop/    Electron wrapper -> Windows .exe/.zip and Linux AppImage/.deb/.rpm/.tar.gz
android/    Android WebView wrapper -> .apk (loads web/ as app assets)
scripts/    make_icons.py regenerates every app icon from the pixel cat sprite
```

`web/neko-run.js` is the single source of the game. The website copies it to `Nekomo-Main-Web/neko-run.js` and embeds it with:

```html
<div data-neko-run data-prefix="nekomo_404_"></div>
<script src="/neko-run.js" defer></script>
```

or from JS: `NekoRun.mount(element, { prefix, mode: 'embed' | 'app', fullscreen, desktop, autoFullscreenAfter })`.

## Building

**Play in a browser:** serve `web/` with any static server, e.g. `cd web && python3 -m http.server`, and open http://localhost:8000.

**Windows / Linux** (Node 18+):

```bash
cd desktop
npm install
npm start            # run locally
npm run dist         # Windows installer + portable exe -> desktop/dist
npm run dist:linux   # AppImage + .deb -> desktop/dist
```

Building the Windows exe on Linux needs Wine; the easiest way is electron-builder's Docker image:

```bash
docker run --rm -v "$PWD":/project -w /project/desktop electronuserland/builder:wine \
  bash -c "npm install && npm run dist"
```

**Android** (JDK 17, Android SDK 34):

```bash
cd android
echo "sdk.dir=$HOME/Android/Sdk" > local.properties
./gradlew assembleRelease
```

The APK lands in `android/app/build/outputs/apk/release/`. To sign it, create `android/keystore.properties` (git-ignored):

```properties
storeFile=/path/to/neko-run-release.jks
storePassword=...
keyAlias=nekorun
keyPassword=...
```

or set `NEKORUN_STORE_FILE`, `NEKORUN_STORE_PASSWORD`, `NEKORUN_KEY_ALIAS` and `NEKORUN_KEY_PASSWORD`. Without a key the release APK is unsigned.

## Credits

Pixel font: [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) by CodeMan38, SIL Open Font License (`web/fonts/OFL.txt`).
