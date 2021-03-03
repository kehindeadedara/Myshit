function validate() {  
	var result = "";	
	result += validateName(); 	
	result += validateEmail();
	result += validateTerms();
	result += validateBox();
	if (result == "") return true;
	
	alert("Validation Error:\n\n" + result);
	return false;	
}

function validateName() {
	var name = document.getElementsByName("name")[0].value;
	if (name.length <= 3)
		return "Name should be at least three characters.\n";	
	return "";
}
function validateBox(){
	var pictureBox1 = document.getElementById("pikachu");
	var pictureBox2 = document.getElementById("gengar");
	var pictureBox3 = document.getElementById("evee");
		if (!pictureBox1.checked || !pictureBox2.checked || !pictureBox3.checked )
		return "Please select a picture for authentication";	
	return "";
}


function validateEmail() {
	var email = valueOf("email");
	var email2 = valueOf("retype_email");
	
	if (email.indexOf('@') == -1) 
		return "Email should be a valid address.\n";
	
	if (email != email2)
		return "Email addresses do not match.\n";
	return "";	
}

function validateTerms() {
	var terms = document.getElementsByName("terms")[0];
	if (!terms.checked)
		return "Please accept the Terms of Service and Privacy Policy.\n";	
	return "";
}

function valueOf(name) {
	return document.getElementsByName(name)[0].value;
}