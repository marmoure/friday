const path = require("path");

const express = require("express");

const app = express();

const server = require('http').createServer(app);
const io = require('socket.io')(server);

app.use(express.static(path.join(__dirname,"public")));

app.use((req, res ,next) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

server.listen(3000,() => {
    console.log("running...");
});


io.on('connect', (socket) => {
    socket.on("wow",(msg) => {
        console.log("little hope made it");
    })
});