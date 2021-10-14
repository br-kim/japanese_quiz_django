function urlToFileName(url){
    let splited_url = url.split("/");
    return splited_url[splited_url.length - 1].split(".")[0];
}

function getCSRFToken(){
    let result = "";
    document.cookie.split("; ").forEach(
        (element)=>{
            if(element.startsWith("csrftoken")) {
                result = element.split("=")[1]
            }});
    return result;
}

function getGanaType(url){
    let new_url = url.split("/");
    return new_url[new_url.length-2];
}