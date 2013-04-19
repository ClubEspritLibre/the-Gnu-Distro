var connected = false;
// état de la connection
var server = "localhost";
// l'adresse du serveur
var port = 9999;
// Le port a utiliser
var socket;

// La fonction connect permet d'initialiser la connexion à travers
// la variable sokcet déclaré plus haut.

function connect() {
	/* TODO */

	socket = new WebSocket("ws://" + server + ":" + port);

	socket.onopen = function(evt) {
		connected = true;
	};

	socket.onclose = function(evt) {
		connected = false;
	};
	socket.onmessage = function(evt) {
    alert(evt.data);
	};
	socket.onerror = function(evt) {

	};

}

/* La fonction sendMSG permet l'envoie de messages au serveur
 grace à la méthode send() de l'objet websocket
 elle prend en paramètre la commande à envoyer au serveur.
 elle sera appelé lorsqu'un évenement est déclaché par l'utilisateur "onClick()".
 Le format de la commande est le suivant :
 CMD:ARG1,ARG2,ARG3,...,ARGN
 aCmd est une chaine de charactères */

function sendCMD(aCmd) {
	if (socket.readyState == 1) {
		socket.send(aCmd);
	}

}

function closeConnection() {
	socket.close();
}


$(document).ready(function() {

	connect();

	$("#copyu").click(function() {
		sendCMD("COPY:UBUNTU");
	});

	$("#copyf").click(function() {
		sendCMD("COPY:FEDORA");
	});

	$("#copym").click(function() {
		sendCMD("COPY:MINT");
	});

	$("#bootu").click(function() {
		sendCMD("BOOT:UBUNTU");
	});

	$("#bootf").click(function() {
		sendCMD("BOOT:FEDORA");
	});

	$("#bootm").click(function() {
		sendCMD("BOOT:MINT");
	});

	//closeConnection();
});

