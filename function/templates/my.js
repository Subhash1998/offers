var info = document.getElementById('info');
var btn = document.getElementById('btn');
btn.addEventListener('click',function(){

		var xhttp = new XMLHttpRequest();
		xhttp.open('GET','http://127.0.0.1:8000/feature_list/?format=json');
		xhttp.onload = function(){
		var data = JSON.parse(xhttp.responseText);
		console.log(data);
		renderHTML(data);
	};
	xhttp.send();
});
var i=0;

function renderHTML(data){
	var htmlString = "";

	for(i=0;i<data.length;i++){
		htmlString += "<p><b>Feature Name  :  </b>" + data[i].feature_name + "</p><p><b>Feature Detail  :  </b>" + data[i].feature_detail + "</p>";
	}
	if(i==data.length)
	{
		document.getElementById('btn').style.display='none';
	}
	info.insertAdjacentHTML('beforeend' , htmlString);
}