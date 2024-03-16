document.getElementById('codeSourceBtn').addEventListener('click', () => {
    require('electron').ipcRenderer.send('open-url', 'https://github.com/DevHollo/hmod-url-protocol/tree/main/src');
});

document.getElementById('allProtocolsBtn').addEventListener('click', () => {
    require('electron').ipcRenderer.send('open-url', 'https://raw.githubusercontent.com/DevHollo/hmod-url-protocol/main/protocols.txt');
});