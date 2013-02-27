

var connected = false      // état de la connection 
var server = "localhost"   // l'adresse du serveur
var socket;


// La fonction connect permet d'initialiser la connexion à travers
// la variable sokcet déclaré plus haut.

function connect(){
  /* TODO */
    
}


/* La fonction sendMSG permet l'envoie de messages au serveur 
   grace à la méthode send() de l'objet websocket
   elle prend en paramètre la commande à envoyer au serveur.
   elle sera appelé lorsqu'un évenement est déclaché par l'utilisateur "onClick()".
   Le format de la commande est le suivant : 
   CMD:ARG1,ARG2,ARG3,...,ARGN
   aCmd est une chaine de charactères */
 
function sendCMD(aCmd){
  if (con.readyState == 1) {
    con.send(aCmd);
}

}
