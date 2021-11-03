let my_client_id = String(Date.now());
document.querySelector("#ws-id").textContent = String(my_client_id);
let websocketScheme = (document.location.protocol === 'http:') ? 'ws' : 'wss';

// let ws_send = new WebSocket(`${websocketScheme}://${document.location.host}/chatting/${my_client_id}/send`,);
// let ws_receive = new WebSocket(`${websocketScheme}://${document.location.host}/chatting/${my_client_id}/receive`,);
let ws_send = new WebSocket(`${websocketScheme}://${document.location.host}/ws/chatting/room`);
let ws_receive = ws_send


ws_receive.onclose = function () {
    ws_receive.send("disconnected");
};

ws_receive.onmessage = function (event) {
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

    if (data.type === 'list'){
        data.message.forEach((elem)=>{
            let node = createUserName(elem);
            document.getElementById('chatting-users-div').append(node);
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

ws_send.onopen = ()=>{
    ws_send.send(JSON.stringify(
        {
            user_id:my_client_id,
        }
    ));
    let a = function () {
        setTimeout(a,40000);
        ws_send.send(JSON.stringify({
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
        if (!document.getElementById(node.id)) {
            document.getElementById('chatting-users-div').append(node);
        }
    }
    else if(data.detail ==='leave'){
        if(document.getElementById(data.sender)) {
            document.getElementById(data.sender).remove();
        }
        if(data.sender === my_client_id){
            ws_receive.close();
        }
    }
}

function sendMessage(event) {
    let input = document.getElementById("messageText");
    let target = document.getElementById("sendTo");
    ws_send.send(
        JSON.stringify({
            type: "message",
            sender: my_client_id,
            message: input.value,
            receiver: target.value
        }));
    input.value = '';
    event.preventDefault();
}
