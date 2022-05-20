//const path = require('path')
const electron = require('electron');
const techacademy = electron.app;
const BrowserWindow = electron.BrowserWindow;
let mainWindow;

//const  electronReload  =  require('electron-reload')

techacademy.on('ready', function() {
  let subpy = require('child_process').spawn('python',['./index.py']);
  let URL = 'http://localhost:5000';

  let openWindow = function() {
  mainWindow = new BrowserWindow({width: 1000, height: 600 });
  mainWindow.loadURL(URL);
  mainWindow.webContents.openDevTools()
  };
  openWindow();
});