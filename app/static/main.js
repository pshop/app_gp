    const buttonSubmit = document.querySelector("#submit");
    const inputQuestion = document.querySelector("#question");

    buttonSubmit.addEventListener("click", ()=>{
        loadXMLDoc(inputQuestion.value);
    });
    document.addEventListener("keydown", (e)=>{
        if (e.key === "Enter"){
            e.preventDefault();
            loadXMLDoc(inputQuestion.value)
        }

    });
    
    function loadXMLDoc(value)
    {
        var req = new XMLHttpRequest();
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
                    injectQR(response.question, response.response1, response.response2)
                }
            }
        });
    
        req.open('POST', '/ajax');
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        const postVars = 'question='+value;
        req.send(postVars);
        
        return false;
    }

    function injectQR(question, response1, response2){
        const container = document.createElement("div");
        container.className = "qr";

        const contQuestion = document.createElement("div");
        contQuestion.className = "q";
        contQuestion.innerHTML = question;

        const constReponse1 = document.createElement("div");
        constReponse1.className = "r" ;
        constReponse1.innerHTML = response1;

        const constReponse2 = document.createElement("div");
        constReponse2.className = "r" ;
        constReponse2.innerHTML = response2;

        container.appendChild(contQuestion);
        container.appendChild(constReponse1);
        container.appendChild(constReponse2);

        document.querySelector("#chat").appendChild(container);

     }
