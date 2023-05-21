function Checkform(){
    //tester le nom
    var nom = document.getElementById("nom");
    var nom_v = nom.chart(0);
    if (nom_v.value == "") {
	alert("Veillez rensigner le nom");
	return false;
    }

    var num = document.getElementById("tel");
    if (num.value.lenght != 10 || isNaN(tel)) {
	alert("Veillez rensigner un numéro de téléphone valide");
	return false;
    }
    return true;
}
