
window.onload = function(e){
	document.getElementById("id_is_staff").addEventListener("click", onclickchange);
	function onclickchange(){
		var x = document.getElementById("id_groups").options[0];
		var y = x.selected;
		x.selected = !y;
	}
	document.getElementsByClassName("form-row field-groups")[0].style.display = "none";
}