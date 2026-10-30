const { contextBridge } = require('electron');

contextBridge.exposeInMainWorld('nekoRunHost', { platform: 'desktop', versions: { electron: process.versions.electron } });
