function toggleClass(name, object){
    if(object.className == name){
        object.className = ""
    }else{
        object.className = name
        console.log(object.className);
    }
}

function nav(){
    navigation = document.getElementById("nav");
    navBtn = document.getElementById("nav-btn");
    body = document.getElementsByTagName("body")
    toggleClass("nav-btn-active", navBtn)
    toggleClass("visible", navigation);
    toggleClass("no-overflow", body[0])
}

