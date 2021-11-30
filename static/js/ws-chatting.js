let my_client_id = String(Date.now());

let websocketScheme = (document.location.protocol === 'http:') ? 'ws' : 'wss';

let ws_connection = new WebSocket(`${websocketScheme}://${document.location.host}/ws/chatting/room`);

function addUserList(node){
    if (!document.getElementById(node.id)) {
        console.log(document.getElementById(node.id));
        document.getElementById('chatting-users-div').append(node);
    }
}

ws_connection.onclose = function () {
    alert("연결이 종료되었습니다.");
};

ws_connection.onmessage = function (event) {
    let messages = document.getElementById('messages');
    let message = document.createElement('li');
    let data = JSON.parse(event.data);
    /**
     * @param data
     * @param data.client_id
     * @param data.message
     * @param data.type
     * @param data.sender
     * @param data.detail
     * **/
    let content = document.createTextNode(data.message);
    let messageHeader = "";
    if (data.type === 'keepalive'){
        return;
    }

    if (data.type === 'user_id') {
        my_client_id = data.message;
        document.querySelector("#ws-id").textContent = String(my_client_id);
        return;
    }

    if (data.type === 'list'){
        data.message.forEach((elem)=>{
            let node = createUserName(elem);
            addUserList(node);
        });
        return;
    }

    if (data.type === 'whisper'){
        if (data.sender === my_client_id){
            messageHeader = document.createTextNode("to " + data.sender + " : ");
        }else{
            messageHeader = document.createTextNode("from " + data.sender + " : ");
        }
    }

    if (data.type === 'message'){
        if (data.sender === my_client_id){
            messageHeader = document.createTextNode("Your Message"+ " : ");
        }else{
            messageHeader = document.createTextNode(data.sender + " : ");
        }
    }

    if (data.type === 'alert') {
        processAlert(data);
        messageHeader = data.sender+" ";
    }

    message.append(messageHeader, content);
    messages.appendChild(message);
    document.querySelector("#messages-div").scrollTop =
        document.querySelector("#messages-div").scrollHeight;
};

ws_connection.onopen = ()=>{
    let a = function () {
        setTimeout(a,40000);
        ws_connection.send(JSON.stringify({
            keepalive: true
        }));
    };
    a();
};

function createUserName(client_id){
    let node = document.createElement('div');
    node.textContent = client_id;
    if(client_id === my_client_id){
        node.textContent += '(나)';
    }
    node.id = client_id;
    node.addEventListener('click',()=>{
        document.getElementById('sendTo').value = client_id;
    });
    return node;
}

function processAlert(data){
    if (data.detail === 'enter'){
        let node = createUserName(data.sender);
        addUserList(node);
    }
    else if(data.detail ==='leave'){
        if(document.getElementById(data.sender)) {
            document.getElementById(data.sender).remove();
        }
        if(data.sender === my_client_id){
            ws_connection.close();
        }
    }
}

function sendMessage(event) {
    let input = document.getElementById("messageText");
    let target = document.getElementById("sendTo");
    let messageType;

    if (target.value){
        messageType = "whisper";
    }
    else{
        messageType = "message";
    }
    ws_connection.send(
        JSON.stringify({
            type: messageType,
            sender: my_client_id,
            message: input.value,
            receiver: target.value
        }));
    input.value = '';
    event.preventDefault();
}
