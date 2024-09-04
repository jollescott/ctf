class Terminal {
    #socket;
    #responseListeners;

    constructor(taskId) {
        this.taskId = taskId;
        this.#socket = new WebSocket("ws://" + window.location.host + '/ws/terminal/' + taskId + '/');
        this.#responseListeners = [];

        this.#socket.onmessage = (e) => this.#handleMessage(e.data);
        this.#socket.onopen = (e) => console.log("Terminal connected!");
    }

    #handleMessage(data) {
        this.#responseListeners.forEach(l => l(data));
    }

    send(command) {
        const message = JSON.stringify({
            "command": command
        });

        this.#socket.send(message);
    }

    addResponseListener(listener) {
        this.#responseListeners.push(listener);
    }
}