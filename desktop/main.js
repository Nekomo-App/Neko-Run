const { app, BrowserWindow, Menu, shell } = require('electron');
const path = require('path');

if (!app.requestSingleInstanceLock()) app.quit();

let win;

function createWindow() {
    win = new BrowserWindow({
        width: 1100,
        height: 520,
        minWidth: 480,
        minHeight: 260,
        backgroundColor: '#0c0508',
        title: 'Neko Run',
        icon: path.join(__dirname, 'app', 'icon.png'),
        autoHideMenuBar: true,
        show: false,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
            nodeIntegration: false,
            sandbox: true
        }
    });
    Menu.setApplicationMenu(null);
    win.loadFile(path.join(__dirname, 'app', 'index.html'), { query: { platform: 'desktop' } });
    win.once('ready-to-show', () => win.show());
    win.webContents.setWindowOpenHandler(({ url }) => {
        if (/^https?:/.test(url)) shell.openExternal(url);
        return { action: 'deny' };
    });
    win.webContents.on('will-navigate', (e, url) => {
        if (!url.startsWith('file:')) e.preventDefault();
    });
    win.webContents.on('before-input-event', (e, input) => {
        if (input.type === 'keyDown' && input.key === 'F11') {
            win.setFullScreen(!win.isFullScreen());
            e.preventDefault();
        }
    });
}

app.on('second-instance', () => {
    if (win) { if (win.isMinimized()) win.restore(); win.focus(); }
});
app.whenReady().then(createWindow);
app.on('window-all-closed', () => app.quit());
