// Copies the shared game from ../web into ./app so Electron packages exactly what the website runs.
const fs = require('fs');
const path = require('path');

const src = path.join(__dirname, '..', '..', 'web');
const dest = path.join(__dirname, '..', 'app');
fs.rmSync(dest, { recursive: true, force: true });
// web/package.json is the npm package manifest; leaving it in app/ would make electron-builder treat app/ as the app.
fs.cpSync(src, dest, { recursive: true, filter: (f) => f !== path.join(src, 'package.json') });
console.log('copied web ->', path.relative(process.cwd(), dest));
