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
    toggleClass("visible", navigation); 
}

