const taskId = document.currentScript.dataset.taskId;

const testSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/test'
);

testSocket.onmessage = function (e) {
    const node = document.createElement('p');
    node.innerText = e.data;

    document.body.appendChild(node);
}

function askForSecret() {
    testSocket.send(JSON.stringify({
        'task_id': taskId
    }));
}