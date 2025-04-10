const symbols = ['🍒', '🍋', '🍉', '⭐', '🍇', '🔔'];
let balance = 1000;


function addMoney(){
    let depositInput = document.getElementById("deposit");
    let deposit = parseInt(depositInput.value);
    if(deposit > 0){
        balance += deposit;
        document.getElementById("currentBalance").textContent = balance;
    }else{
        alert("Zadejte platnou částku!");
    }

}

function spin(){
    let bet = parseInt(document.getElementById("bet").value);
    let spinSound = document.getElementById("spinSound");
}
