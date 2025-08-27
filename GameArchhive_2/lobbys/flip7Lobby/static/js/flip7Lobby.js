export const socket = io();

socket.on('redirect', ({ url }) => { window.location.href = url; });