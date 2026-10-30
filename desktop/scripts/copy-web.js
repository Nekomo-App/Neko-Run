// Copies the shared game from ../web into ./app so Electron packages exactly what the website runs.
const fs = require('fs');
const path = require('path');

const src = path.join(__dirname, '..', '..', 'web');
const dest = path.join(__dirname, '..', 'app');
fs.rmSync(dest, { recursive: true, force: true });
fs.cpSync(src, dest, { recursive: true });
console.log('copied web ->', path.relative(process.cwd(), dest));
