function getCSRFToken(){
    let result = "";
    document.cookie.split("; ").forEach(
        (element)=>{
            if(element.startsWith("csrftoken")) {
                result = element.split("=")[1]
            }});
    return result;
}