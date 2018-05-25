const buttonSubmit = document.querySelector("#submit");
const inputQuestion = document.querySelector("#question");
const containerChat = document.querySelector("#chat");
const animation = document.querySelector("#animation");

buttonSubmit.addEventListener("click", ()=>{
    sendMsg();
});
document.addEventListener("keydown", (e)=>{
    if (e.key === "Enter"){
        e.preventDefault();
        sendMsg();
    }
});

function sendMsg() {
    const msgClient = clearTextArea(inputQuestion);

    const msgClientElementContainer = document.createElement("div");
    msgClientElementContainer.className = "q-container";

    const msgClientElement = document.createElement("div");
    msgClientElement.className = "q" ;
    msgClientElement.innerText = msgClient;

    msgClientElementContainer.appendChild(msgClientElement);

    containerChat.appendChild(msgClientElementContainer);

    animation.classList.remove("speak");
    animation.classList.add("wait");

    scrollDown();

    loadXMLDoc(msgClient);
}

function loadXMLDoc(value)
{
    const req = new XMLHttpRequest();
    req.addEventListener("readystatechange", ()=>{
        if (req.readyState === 4)
        {
            if (req.status != 200)
            {
                console.error(req.status)
            }
            else
            {
                const response = JSON.parse(req.responseText);
                console.log(response);
                injectQR(response.response1, response.image, response.response2);
                animation.classList.remove("wait");
                animation.classList.add("speak");
            }
        }
    }, true);

    req.open('POST', '/ajax');
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    const postVars = 'question='+value;
    req.send(postVars);
    
    return false;
}

/**
 * @param response1 string
 * @param image string - maps url
 * @param response2 string
 */
function injectQR(response1, image, response2){
    // response 1
    const constReponse1ElementContainer = document.createElement("div");
    constReponse1ElementContainer.className = "r-container";

    const constReponse1 = document.createElement("div");
    constReponse1.className = "r" ;
    constReponse1.innerHTML = response1;

    // image
    const imgContainer = document.createElement("div");
    imgContainer.className = "r-container img";

    const constReponseImg = document.createElement("div");
    constReponseImg.className = "r img" ;

    const img = document.createElement("img");
    img.src = image;

    // response 2
    const constReponse2ElementContainer = document.createElement("div");
    constReponse2ElementContainer.className = "r-container";

    const constReponse2 = document.createElement("div");
    constReponse2.className = "r" ;
    constReponse2.innerHTML = response2;

    // inject msg in view
    constReponse1ElementContainer.appendChild(constReponse1);
    constReponseImg.appendChild(img);
    imgContainer.appendChild(constReponseImg);
    constReponse2ElementContainer.appendChild(constReponse2);

    containerChat.appendChild(constReponse1ElementContainer);
    containerChat.appendChild(imgContainer);
    containerChat.appendChild(constReponse2ElementContainer);

    scrollDown();
 }

/**
 * @return string - return content of area
 * @param areaElement HTMLAreaElement - area ellement to clear. default: area[0] in dom
 */
function clearTextArea(areaElement= document.querySelector("textarea")) {
    const contentToReturn = areaElement.value;
    areaElement.value = "";
    return contentToReturn.replace(/</g,"&lt;").replace(/>/g,"&gt;");;
 }

 function scrollDown() {
     containerChat.scrollTop = containerChat.scrollHeight;
 }
